from unittest import TestCase

from BernsteinVazirani.BernsteinVazirani import BernsteinVazirani
from utils import dotdict


class TestBernsteinVazirani(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "qasm_simulator"
        args.shots = 500
        args.bernstein_vazirani_s = '10011010101101'
        self.args = args

    def test(self):
        self.args.deutsch_jozsa_oracle = 'balanced'
        alg = BernsteinVazirani(self.args)
        results = alg.run()
        print(results)
        self.assertEqual(results.get_counts(alg.circuit)[self.args.bernstein_vazirani_s], self.args.shots)
