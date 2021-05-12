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
    """default 2 Qubits"""
    qubits = 2

    def __init__(self, args):
        if self.args.qubits:
            self.qubits = self.args.qubits
        super().__init__("Grover Algorithm", args)

    def get_qubits(self):
        return self.qubits

    def diffuser(self):
        qc = QuantumCircuit(self.qubits)
        # Apply transformation |s> -> |00..0> (H-gates)
        for qubit in range(self.qubits):
            qc.h(qubit)
        # Apply transformation |00..0> -> |11..1> (X-gates)
        for qubit in range(self.qubits):
            qc.x(qubit)
        # Do multi-controlled-Z gate
        qc.h(self.qubits - 1)
        qc.mct(list(range(self.qubits - 1)), self.qubits - 1)  # multi-controlled-toffoli
        qc.h(self.qubits - 1)
        # Apply transformation |11..1> -> |00..0>
        for qubit in range(self.qubits):
            qc.x(qubit)
        # Apply transformation |00..0> -> |s>
        for qubit in range(self.qubits):
            qc.h(qubit)
        # We will return the diffuser as a gate
        U_s = qc.to_gate()
        U_s.name = "U$_s$"
        return U_s

