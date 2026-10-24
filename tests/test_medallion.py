import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import medallion as m


class MedallionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        self.root.mkdir()
        self.src = Path(self.tmp.name) / 'source'
        self.src.mkdir()
        (self.src / 'chart.py').write_text('def render(data, theme, context):\n    return None\n')
        (self.src / 'data.csv').write_text('category,value\nExample,1\n')
        m.write(self.src / 'config.json', {'THEME': {'source': {}, 'neutral': {}}, 'CONTEXT': {}})
        m.write(self.src / 'record.json', {'source_url': 'https://example.org/chart', 'validation_status': 'verified'})
        self.bundle = m.ingest(self.root, self.src, '2026-10-25', 'example')
        self.relative = str(self.bundle.relative_to(self.root))
        self.digest = m.validate_bundle(self.bundle)['payload_sha256']
        event = Path(self.tmp.name) / 'event.json'
        m.write(event, {'inputs': {'approved': 'true', 'notes': 'TEST FIXTURE ONLY'}})
        self.env = {'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REPOSITORY': m.REPOSITORY,
                    'GITHUB_REF': 'refs/heads/main', 'GITHUB_ACTOR': m.OWNER,
                    'GITHUB_TRIGGERING_ACTOR': m.OWNER, 'GITHUB_EVENT_PATH': str(event),
                    'GITHUB_RUN_ID': '123', 'GITHUB_SHA': 'test-commit'}

    def test_initial_is_bronze_even_if_agent_verified(self):
        c = m.catalog(self.root)
        self.assertEqual(c['counts'], {'bronze': 1, 'silver': 0, 'gold': 0})
        self.assertFalse(c['templates'][0]['training_eligible'])

    def test_idempotent_ingest(self):
        self.assertEqual(self.bundle, m.ingest(self.root, self.src, '2026-10-25', 'example'))

    def test_revision_preserves_original(self):
        (self.src / 'data.csv').write_text('category,value\nExample,2\n')
        revision = m.ingest(self.root, self.src, '2026-10-25', 'example')
        self.assertNotEqual(self.bundle, revision)
        self.assertEqual(m.validate_bundle(self.bundle)['payload_sha256'], self.digest)

    def test_changed_payload_invalidates_snapshot(self):
        (self.bundle / 'data.csv').write_text('tampered')
        with self.assertRaises(ValueError):
            m.validate_bundle(self.bundle)

    def test_no_automatic_approval(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(ValueError):
            m.promote(self.root, self.relative, 'silver', self.digest)

    def test_wrong_reviewer(self):
        env = dict(self.env, GITHUB_ACTOR='other-user')
        with patch.dict(os.environ, env, clear=True), self.assertRaises(ValueError):
            m.promote(self.root, self.relative, 'silver', self.digest)

    def test_wrong_reviewed_hash(self):
        with patch.dict(os.environ, self.env, clear=True), self.assertRaises(ValueError):
            m.promote(self.root, self.relative, 'silver', '0' * 64)

    def test_bronze_cannot_skip_silver(self):
        with patch.dict(os.environ, self.env, clear=True), self.assertRaises(ValueError):
            m.promote(self.root, self.relative, 'gold', self.digest)

    def test_valid_silver_preserves_bronze(self):
        with patch.dict(os.environ, self.env, clear=True):
            target = m.promote(self.root, self.relative, 'silver', self.digest)
        self.assertEqual(m.validate_bundle(target)['tier'], 'silver')
        self.assertEqual(m.validate_bundle(self.bundle)['tier'], 'bronze')
        self.assertEqual(m.catalog(self.root)['counts']['silver'], 1)

    def test_gold_requires_quality_evidence(self):
        with patch.dict(os.environ, self.env, clear=True):
            target = m.promote(self.root, self.relative, 'silver', self.digest)
            with self.assertRaises((ValueError, FileNotFoundError)):
                m.promote(self.root, str(target.relative_to(self.root)), 'gold', self.digest)

    def test_approval_checkbox_required(self):
        m.write(Path(self.env['GITHUB_EVENT_PATH']), {'inputs': {'approved': 'false'}})
        with patch.dict(os.environ, self.env, clear=True), self.assertRaises(ValueError):
            m.promote(self.root, self.relative, 'silver', self.digest)

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            m.bundle_path(self.root, '../outside')


if __name__ == '__main__':
    unittest.main()
