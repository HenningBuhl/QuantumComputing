from subprocess import check_output
import qiskit as q
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import json
import os
import time

# Imports
from qiskit import IBMQ, Aer, assemble
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy
import qiskit as q
import os


class QuantumAlgorithm:
    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.circuit = self.get_circuit()
        self.backend = self.get_backend()
        self.result = None

    def get_circuit(self):
        pass

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

    def save_results(self):
        jsonStr = json.dumps(self.result.data())
        print(jsonStr)
        base_path = 'results/'
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        time_stamp = time.strftime("%Y.%m.%d-%H.%M.%S")
        text_file = open(base_path + self.name + '_' + time_stamp + '.txt', 'w')
        text_file.write(jsonStr)
        text_file.close()

    def save_result_img(self, path, result):
        plot_histogram(result.get_counts()).savefig(path + '.pdf')

    def run_experiments(self):
        base_path = 'results/'
        if not os.path.exists(base_path):
            os.mkdir(base_path)
        self.backend = q.Aer.get_backend(self.args.local_backend)
        result = self.run()
        self.save_result_img(base_path + self.name + '_local', result)

        # run on remote

        IBMQ.save_account(open("token.txt", "r").read())
        factory = IBMQ.load_account()
        devices = factory.backends(filters=lambda x: x.configuration().n_qubits >= 3 and
                                                     not x.configuration().simulator)
        self.backend = least_busy(devices)
        result = self.run()
        self.save_result_img(base_path + self.name + '_remote', result)

