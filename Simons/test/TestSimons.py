from unittest import TestCase

from Simons.Simons import Simons
from utils import dotdict


class TestSimons(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "qasm_simulator"
        args.shots = 500
        args.simons_b = '110'
        self.args = args

    def test_balanced(self):
        alg = Simons(self.args)
        results = alg.run()
        print(results)
        print(results.get_counts())
        b = alg.get_b_from_counts(results.get_counts())
        self.assertEqual(self.args.simons_b, b)
