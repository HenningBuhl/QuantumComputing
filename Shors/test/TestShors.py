from unittest import TestCase

from Shors.Shors import Shors
from utils import dotdict


class TestShors(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "qasm_simulator"
        args.shots = 500
        self.args = args

    def test_shors(self):

        # alg = DeutschJozsa(self.args)
        # results = alg.run()
        pass
