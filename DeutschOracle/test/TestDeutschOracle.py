from unittest import TestCase

from DeutschOracle.DeutschOracle import DeutschOracle
from utils import dotdict


class TestDeutschOracle(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "qasm_simulator"
        args.shots = 500
        args.deutsch_jozsa_n = 3
        args.deutsch_jozsa_oracle = 'constant'  # balanced or constant
        self.args = args

    def test_balanced(self):
        self.args.deutsch_jozsa_oracle = 'balanced'
        alg = DeutschOracle(self.args)
        results = alg.run()
        self.assertEqual(results.get_counts(alg.circuit)['1' * self.args.deutsch_jozsa_n], self.args.shots)

    def test_constant(self):
        self.args.deutsch_jozsa_oracle = 'constant'
        alg = DeutschOracle(self.args)
        results = alg.run()
        self.assertEqual(results.get_counts(alg.circuit)['0' * self.args.deutsch_jozsa_n], self.args.shots)
