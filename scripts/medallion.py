#!/usr/bin/env python3
"""Immutable chart bundles, explicit human review, and reproducible catalogs.

Ingest/validate/promote only read text; they never execute template code.
Promotion is intentionally restricted to the owner's manual GitHub workflow.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
TIERS = ('bronze', 'silver', 'gold')
OWNER = 'UnemployedUncle'
REPOSITORY = OWNER + '/McKinseyGraphTemplates'
ALLOWED = {'chart.py', 'data.csv', 'config.json', 'card.md', 'requirements.txt',
           'record.json', 'validation.json', 'quality.json'}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(files: dict[str, str]) -> str:
    raw = json.dumps(files, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def hashes(folder: Path) -> dict[str, str]:
    result = {}
    for p in sorted(folder.iterdir()):
        if p.name == 'manifest.json':
            continue
        if p.is_symlink() or not p.is_file() or p.name not in ALLOWED:
            raise ValueError(f'Unexpected bundle file: {p.name}')
        result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def bundle_path(root: Path, relative: str) -> Path:
    p = root / relative
    if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):
        raise ValueError('Bundle path escapes repository')
    if Path(relative).parts[0] not in TIERS:
        raise ValueError('Bundle must be under bronze, silver, or gold')
    return p


def validate_bundle(folder: Path) -> dict:
    m = load(folder / 'manifest.json')
    files = hashes(folder)
    if files != m['files'] or digest(files) != m['payload_sha256']:
        raise ValueError(f'Payload changed after snapshot: {folder}')
    if 'chart.py' not in files or m['tier'] not in TIERS:
        raise ValueError('Missing chart.py or invalid tier')
    ast.parse((folder / 'chart.py').read_text(encoding='utf-8-sig'))
    for name in files:
        if name.endswith('.json'):
            load(folder / name)
    if m.get('contract') == 'render-v1':
        if not {'config.json', 'data.csv', 'record.json'} <= files.keys():
            raise ValueError('Incomplete render bundle')
        cfg = load(folder / 'config.json')
        if not {'source', 'neutral'} <= cfg.get('THEME', {}).keys() or 'CONTEXT' not in cfg:
            raise ValueError('Two themes and CONTEXT are required')
    review = m['human_review']
    if m['tier'] == 'bronze':
        if review['status'] != 'pending':
            raise ValueError('Bronze is not a human-approved tier')
    else:
        if review['status'] != 'approved' or review['reviewer'] != OWNER:
            raise ValueError('An owner approval is required')
        if review.get('payload_sha256') != m['payload_sha256']:
            raise ValueError('Approval is for different bytes')
        prefix = f'https://github.com/{REPOSITORY}/actions/runs/'
        if not str(review.get('evidence_url', '')).startswith(prefix):
            raise ValueError('Missing manual workflow audit URL')
        if not m.get('parent', {}).get('path'):
            raise ValueError('Missing parent snapshot')
    return m


def ingest(root: Path, source: Path, date: str, slug: str) -> Path:
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date) or not re.fullmatch(r'[a-z0-9_\-]+', slug):
        raise ValueError('Invalid date or slug')
    datetime.strptime(date, '%Y-%m-%d')
    if not source.is_dir() or source.is_symlink():
        raise ValueError('Source must be a real bundle directory')
    files = {p.name: p for p in source.iterdir() if p.name in ALLOWED}
    if not {'chart.py', 'data.csv', 'config.json', 'record.json'} <= files.keys():
        raise ValueError('Required source files are missing')
    if any(p.is_symlink() or not p.is_file() for p in files.values()):
        raise ValueError('No symlinks or directories allowed')
    checksums = {name: hashlib.sha256(p.read_bytes()).hexdigest() for name, p in files.items()}
    checksum = digest(checksums)
    dest = root / 'bronze' / date / slug
    if dest.exists():
        existing = validate_bundle(dest)
        if existing['payload_sha256'] == checksum:
            return dest
        dest = dest.with_name(slug + '_rev_' + checksum[:12])
        if dest.exists():
            if validate_bundle(dest)['payload_sha256'] == checksum:
                return dest
            raise ValueError('Revision path collision')
    dest.mkdir(parents=True)
    try:
        for name, p in files.items():
            shutil.copyfile(p, dest / name)
        record = load(dest / 'record.json')
        m = {'schema_version': '1.0.0', 'template_id': date.replace('-', '') + '_' + dest.name,
             'tier': 'bronze', 'contract': 'render-v1',
             'ingested_at': datetime.now(timezone.utc).isoformat(),
             'source_url': record.get('source_url'), 'figure_ref': record.get('figure_ref'),
             'human_review': {'status': 'pending', 'reviewer': None}, 'parent': None,
             'files': checksums, 'payload_sha256': checksum}
        write(dest / 'manifest.json', m)
        validate_bundle(dest)
    except Exception:
        shutil.rmtree(dest)
        raise
    return dest


def manual_approval() -> dict:
    if os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch':
        raise ValueError('Use the manual Promote reviewed template GitHub Action')
    if os.environ.get('GITHUB_REPOSITORY') != REPOSITORY or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ValueError('Promotion must run on the repository main branch')
    actor = os.environ.get('GITHUB_ACTOR')
    if actor != OWNER or os.environ.get('GITHUB_TRIGGERING_ACTOR', actor) != OWNER:
        raise ValueError('Only the designated human reviewer may promote')
    event = load(Path(os.environ['GITHUB_EVENT_PATH']))
    inputs = event.get('inputs', {})
    if str(inputs.get('approved', '')).lower() != 'true':
        raise ValueError('Explicit personal-review confirmation required')
    run = os.environ.get('GITHUB_RUN_ID', '')
    if not run.isdigit():
        raise ValueError('Missing GitHub run identity')
    return {'status': 'approved', 'reviewer': actor,
            'reviewed_at': datetime.now(timezone.utc).isoformat(),
            'evidence_url': f'https://github.com/{REPOSITORY}/actions/runs/{run}',
            'notes': inputs.get('notes', ''), 'commit_sha': os.environ.get('GITHUB_SHA')}


def promote(root: Path, relative: str, target: str, expected: str) -> Path:
    review = manual_approval()
    src = bundle_path(root, relative)
    m = validate_bundle(src)
    required = {'silver': 'bronze', 'gold': 'silver'}
    if target not in required or m['tier'] != required[target]:
        raise ValueError('Only bronze -> silver -> gold transitions are allowed')
    if m['payload_sha256'] != expected:
        raise ValueError('Reviewed hash differs from current payload')
    if target == 'gold':
        q = load(src / 'quality.json')
        fields = ('render_passed', 'data_checks_passed', 'reuse_test_passed', 'original_comparison_passed')
        if any(q.get(f) is not True for f in fields):
            raise ValueError('Gold requires render, data, reuse and original-comparison checks')
        if not isinstance(q.get('fidelity_score'), (int, float)) or not 4.5 <= q['fidelity_score'] <= 5:
            raise ValueError('Gold requires fidelity >= 4.5/5')
        if not q.get('evidence') or m.get('contract') != 'render-v1':
            raise ValueError('Gold requires evidence and a reusable render-v1 contract')
    base = root / target / m['template_id']
    version = 1
    while (base / f'v{version:03}').exists():
        prior = validate_bundle(base / f'v{version:03}')
        if prior['payload_sha256'] == expected:
            return base / f'v{version:03}'
        version += 1
    dest = base / f'v{version:03}'
    dest.mkdir(parents=True)
    for name in m['files']:
        shutil.copyfile(src / name, dest / name)
    review['payload_sha256'] = expected
    m.update(tier=target, parent={'path': relative, 'payload_sha256': expected}, human_review=review)
    write(dest / 'manifest.json', m)
    validate_bundle(dest)
    return dest


def catalog(root: Path) -> dict:
    entries = []
    for tier in TIERS:
        for p in sorted((root / tier).rglob('manifest.json')):
            m = validate_bundle(p.parent)
            if m['tier'] != tier:
                raise ValueError('Folder tier and manifest tier differ')
            if m.get('parent'):
                parent = validate_bundle(bundle_path(root, m['parent']['path']))
                if parent['payload_sha256'] != m['parent']['payload_sha256']:
                    raise ValueError('Parent lineage mismatch')
            rec = load(p.parent / 'record.json') if (p.parent / 'record.json').exists() else {}
            entries.append({'template_id': m['template_id'], 'tier': tier,
                            'path': str(p.parent.relative_to(root)), 'contract': m['contract'],
                            'payload_sha256': m['payload_sha256'], 'human_review': m['human_review']['status'],
                            'source_url': m.get('source_url'), 'figure_ref': m.get('figure_ref'),
                            'key_message': rec.get('key_message'),
                            'historical_agent_status': rec.get('validation_status', 'unverified'),
                            'historical_agent_score': rec.get('fidelity_score'),
                            'training_eligible': tier == 'gold' and
                            load(p.parent / 'quality.json').get('training_rights_confirmed') is True})
    keys = [e['path'] for e in entries]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate catalog paths')
    counts = {t: sum(e['tier'] == t for e in entries) for t in TIERS}
    value = {'schema_version': '1.0.0', 'counts': counts, 'templates': entries}
    write(root / 'catalog' / 'index.json', value)
    lines = ['# Template catalog', '', '자동 평가와 사용자 검수는 별개입니다. 모든 최초 코드는 Bronze입니다.', '',
             '| Tier | Template | Human review | Historical agent status |', '|---|---|---|---|']
    for e in entries:
        lines.append(f"| {e['tier']} | [{e['template_id']}](../{e['path']}) | {e['human_review']} | {e['historical_agent_status']} |")
    lines += ['', '검수할 정확한 payload_sha256은 각 manifest.json과 index.json에서 확인합니다.', '']
    (root / 'catalog' / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    for t in TIERS:
        rows = [e for e in entries if e['tier'] == t]
        p = root / 'dataset' / (t + '.jsonl')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in rows), encoding='utf-8')
    return value


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('validate')
    sub.add_parser('catalog')
    i = sub.add_parser('ingest')
    i.add_argument('--source', type=Path, required=True)
    i.add_argument('--date', required=True)
    i.add_argument('--slug', required=True)
    r = sub.add_parser('promote')
    r.add_argument('--path', required=True)
    r.add_argument('--target', choices=['silver', 'gold'], required=True)
    r.add_argument('--expected-sha256', required=True)
    args = p.parse_args()
    if args.command == 'ingest':
        print(ingest(ROOT, args.source, args.date, args.slug))
    elif args.command == 'promote':
        print(promote(ROOT, args.path, args.target, args.expected_sha256))
    result = catalog(ROOT)
    print(json.dumps(result['counts']))


if __name__ == '__main__':
    main()
