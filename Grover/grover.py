import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram

from QuantumAlgorithm import QuantumAlgorithm


class Grover(QuantumAlgorithm):
    qubits = 2

    def __init__(self, args):
        super().__init__("Grover Algorithm", args)

    def first(self, qubits=qubits):
        return qubits
