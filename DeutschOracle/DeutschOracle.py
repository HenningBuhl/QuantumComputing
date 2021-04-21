from QuantumAlgorithm import QuantumAlgorithm
import qiskit as q
import numpy as np


class DeutschOracle(QuantumAlgorithm):
    def __init__(self, args):
        super().__init__("Deutsch Oracle", args)

    def get_circuit(self):
        n = self.args.deutsch_jozsa_n
        circuit = q.QuantumCircuit(n+1, n)

        # Apply H-gates
        for qubit in range(n):
            circuit.h(qubit)

        # Put qubit in state |->
        circuit.x(n)
        circuit.h(n)

        # Add oracle
        if self.args.deutsch_jozsa_oracle == 'balanced':
            circuit += self.get_balanced_oracle();
        else:
            circuit += self.get_constant_oracle();

        # Repeat H-gates
        for qubit in range(n):
            circuit.h(qubit)
        circuit.barrier()

        # Measure
        for i in range(n):
            circuit.measure(i, i)

        return circuit

    def get_constant_oracle(self):
        n = self.args.deutsch_jozsa_n
        constant_oracle = q.QuantumCircuit(n+1)
        output = np.random.randint(2)
        if output == 1:
            constant_oracle.x(n)
        return constant_oracle

    def get_balanced_oracle(self):
        n = self.args.deutsch_jozsa_n
        balanced_oracle = q.QuantumCircuit(n+1)
        b_str = "101"

        # Place X-gates
        for qubit in range(len(b_str)):
            if b_str[qubit] == '1':
                balanced_oracle.x(qubit)

        # Use barrier as divider
        balanced_oracle.barrier()

        # Controlled-NOT gates
        for qubit in range(n):
            balanced_oracle.cx(qubit, n)

        balanced_oracle.barrier()

        # Place X-gates
        for qubit in range(len(b_str)):
            if b_str[qubit] == '1':
                balanced_oracle.x(qubit)
        
        return balanced_oracle
