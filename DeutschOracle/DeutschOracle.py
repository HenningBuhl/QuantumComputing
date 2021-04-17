from QuantumAlgorithm import QuantumAlgorithm
import qiskit as q


class DeutschOracle(QuantumAlgorithm):
    def __init__(self, args):
        super().__init__("Deutsch Oracle", args)


    def get_circuit(self):
        circuit = q.QuantumCircuit(2, 2)
        circuit.h(0)
        circuit.cx(0, 1)
        circuit.measure([0, 1], [0, 1])
        return circuit
