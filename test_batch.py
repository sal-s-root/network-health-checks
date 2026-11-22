import unittest
from unittest.mock import patch
from batch import evaluate

class Batch(unittest.TestCase):
    def test_checks_manifest(self):
        with patch('batch.check',return_value={'ok':True}) as check:
            self.assertEqual(evaluate([{'host':'localhost','port':8080}]),[{'ok':True}])
            check.assert_called_once_with('localhost',8080,2.0)
    def test_rejects_bad_port_before_probing(self):
        with patch('batch.check') as check:
            with self.assertRaises(ValueError):
                evaluate([{'host':'localhost','port':0}])
            check.assert_not_called()
    def test_rejects_empty_manifest(self):
        with self.assertRaises(ValueError):
            evaluate([])
