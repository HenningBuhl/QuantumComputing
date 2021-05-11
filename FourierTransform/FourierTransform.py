from QuantumAlgorithm import QuantumAlgorithm
import qiskit as q
from qiskit.converters import circuit_to_gate
import numpy as np


class FourierTransform(QuantumAlgorithm):
    def __init__(self, args):
        super().__init__("Fourier Transform", args)

    def get_circuit(self):
        n = self.args.fourier_transform_n
        qc = q.QuantumCircuit(n)
        qc = self.qft(qc, n)
        return qc

    def swap_registers(self, circuit, n):
        for qubit in range(n // 2):
            circuit.swap(qubit, n - qubit - 1)
        return circuit

    def qft_rotations(self, circuit, n):
        """Performs qft on the first n qubits in circuit (without swaps)"""
        if n == 0:
            return circuit
        n -= 1
        circuit.h(n)
        for qubit in range(n):
            circuit.cp(np.pi / 2 ** (n - qubit), qubit, n)
        # At the end of our function, we call the same function again on
        # the next qubits (we reduced n by one earlier in the function)
        self.qft_rotations(circuit, n)

    def qft(self, circuit, n):
        """QFT on the first n qubits in circuit"""
        self.qft_rotations(circuit, n)
        self.swap_registers(circuit, n)
        return circuit

    def inverse(self, circuit, n):
        """Does the inverse QFT on the first n qubits in circuit"""
        # First we create a QFT circuit of the correct size:
        qft_circ = self.qft(QuantumCircuit(n), n)
        # Then we take the inverse of this circuit
        invqft_circ = qft_circ.inverse()
        # And add it to the first n qubits in our existing circuit
        circuit.append(invqft_circ, circuit.qubits[:n])
        return circuit.decompose()  # .decompose() allows us to see the individual gates
