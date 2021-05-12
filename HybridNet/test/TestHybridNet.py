from unittest import TestCase

import numpy as np
import matplotlib.pyplot as plt

import torch
from torch.autograd import Function
from torchvision import datasets, transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

import qiskit
from qiskit import transpile, assemble
from qiskit.visualization import *

from HybridNet.HybridNet import QuantumCircuit
from utils import dotdict


class TestHybridNet(TestCase):
    def setUp(self):
        args = dotdict()
        args.location = "local"  # local or remote
        args.local_backend = "qasm_simulator"
        args.shots = 500
        args.deutsch_jozsa_n = 3
        args.deutsch_jozsa_oracle = 'constant'  # balanced or constant
        self.args = args

    def test_net(self):
        simulator = qiskit.Aer.get_backend('qasm_simulator')
        circuit = QuantumCircuit(1, simulator, 100)
        print('Expected value for rotation pi {}'.format(circuit.run([np.pi])[0]))
        print(circuit._circuit)
