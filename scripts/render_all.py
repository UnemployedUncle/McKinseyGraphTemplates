#!/usr/bin/env python3
"""Run chart smoke tests without interpreting success as source verification."""
import json
import os
from pathlib import Path
import subprocess
import sys
from medallion import ROOT, TIERS, validate_bundle


def main():
    reports = []
    outroot = ROOT / 'artifacts'
    outroot.mkdir(exist_ok=True)
    for tier in TIERS:
        for manifest in sorted((ROOT / tier).rglob('manifest.json')):
            folder = manifest.parent
            m = validate_bundle(folder)
            if m['contract'] != 'render-v1':
                continue
            out = outroot / tier / m['template_id']
            out.mkdir(parents=True, exist_ok=True)
            for theme in ('source', 'neutral'):
                dest = out / f'{theme}.png'
                command = [sys.executable, str(folder / 'chart.py'), '--data', str(folder / 'data.csv'),
                           '--config', str(folder / 'config.json'), '--theme', theme, '--output', str(dest)]
                env = {k: v for k, v in os.environ.items()
                       if not any(s in k.upper() for s in ('TOKEN', 'SECRET', 'PASSWORD', 'API_KEY'))}
                env['MPLBACKEND'] = 'Agg'
                try:
                    run = subprocess.run(command, cwd=folder, env=env, capture_output=True, text=True, timeout=60)
                    # Older render-v1 templates accept --config, while newer ones
                    # load config.json beside chart.py without a CLI flag.
                    # Retry only for this specific argparse incompatibility.
                    if run.returncode != 0 and 'unrecognized arguments: --config' in run.stderr:
                        flag_index = command.index('--config')
                        fallback_command = command[:flag_index] + command[flag_index + 2:]
                        run = subprocess.run(fallback_command, cwd=folder, env=env,
                                             capture_output=True, text=True, timeout=60)
                    success = run.returncode == 0 and dest.exists() and dest.stat().st_size > 0
                    report = {'template_id': m['template_id'], 'theme': theme, 'success': success,
                              'returncode': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr,
                              'payload_sha256': m['payload_sha256']}
                except subprocess.TimeoutExpired:
                    report = {'template_id': m['template_id'], 'theme': theme, 'success': False, 'error': 'timeout'}
                reports.append(report)
                print(json.dumps({k: report[k] for k in ('template_id', 'theme', 'success')}))
    (outroot / 'smoke_test_results.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
    if any(not r['success'] for r in reports):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
