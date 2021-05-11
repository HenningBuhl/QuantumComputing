from unittest import TestCase

from FourierTransform.FourierTransform import FourierTransform
from utils import dotdict


class TestFourierTransform(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "statevector_simulator"
        args.shots = 500
        self.args = args

    def test_transform(self):
        self.args.fourier_transform_n = 3
        alg = FourierTransform(self.args)
        results = alg.run()
        print(results.get_statevector())
        print(alg.circuit)
        #self.assertEqual(results.get_counts(alg.circuit)['1' * self.args.deutsch_jozsa_n], self.args.shots)
