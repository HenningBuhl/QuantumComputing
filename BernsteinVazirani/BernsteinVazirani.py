from QuantumAlgorithm import QuantumAlgorithm
import qiskit as q
import numpy as np


class BernsteinVazirani(QuantumAlgorithm):
    def __init__(self, args):
        super().__init__("Bernstein Vazirani", args)

    def get_circuit(self):
        s = self.args.bernstein_vazirani_s
        n = len(s)
        circuit = q.QuantumCircuit(n + 1, n)
        #s += 'b'

        # Put auxiliary in state |->
        circuit.h(n)
        circuit.z(n)

        # Apply Hadamard gates before querying the oracle
        for i in range(n):
            circuit.h(i)

        # Apply barrier
        circuit.barrier()

        # Apply the inner-product oracle
        s = s[::-1]  # reverse s to fit qiskit's qubit ordering
        for _q in range(n):
            if s[_q] == '0':
                circuit.i(_q)
            else:
                circuit.cx(_q, n)

        # Apply barrier
        circuit.barrier()

        # Apply Hadamard gates after querying the oracle
        for i in range(n):
            circuit.h(i)

        # Measurement
        for i in range(n):
            circuit.measure(i, i)

        return circuit
