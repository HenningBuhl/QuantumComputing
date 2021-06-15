from unittest import TestCase

from Grover import grover
from Grover.grover import Grover
from utils import dotdict


class TestGrover(TestCase):

    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "statevector_simulator"
        args.shots = 500
        self.args = args



    def test_transform(self):

        alg = Grover(self.args)
        results = alg.groverFull()
        print(results.get_statevector())
        print(alg.circuit)

