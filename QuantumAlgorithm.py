from subprocess import check_output
import qiskit as q
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class QuantumAlgorithm:
    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.circuit = self.get_circuit()
        self.backend = self.get_backend()
        self.result = None

    def get_backend(self):
        if self.args.location == "local":
            # Run locally.
            backend = q.Aer.get_backend(self.args.local_backend)
        else:
            # Run on backend.
            IBMQ.save_account(open("token.txt", "r").read())
            IBMQ.load_account()
            provider = IBMQ.get_provider("ibm-q")
            for backend in provider.backends():
                try:
                    qubit_count = len(backend.properties().qubits)
                except:
                    qubit_count = "simulated"
                print(f"{backend.name():35} has {backend.status().pending_jobs:8} queued and {qubit_count:12} qubits")
            backend = ""
        return backend

    def run(self):
        job = q.execute(self.circuit, backend=self.backend, shots=self.args.shots)
        job_monitor(job)
        result = job.result()
        self.result = result
        return result

    def save_results(self, file_path):
        pass  # TODO
