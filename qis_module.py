# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute, register

from math import pi

from utils import *

from Qconfig import APItoken

def qis_module_init():

    if IBM_BACKEND:
        QX_TOKEN = APItoken
        QX_URL = "https://quantumexperience.ng.bluemix.net/api"

        # Authenticate with the IBM Q API in order to use online devices.
        # You need the API Token and the QX URL.
        register(QX_TOKEN, QX_URL)

def Vqe_h2_task(theta, measure_task):
    # Create a Quantum Register with 2 qubits.
    q = QuantumRegister(2)
    # Create a Classical Register with 2 bits.
    c = ClassicalRegister(2)
    # Create a Quantum Circuit
    qc = QuantumCircuit(q, c)

    qc.rx(pi, q[0])

    qc.ry(0.5 * pi, q[1])
    qc.rx(-0.5 * pi, q[0])

    qc.cx(q[1], q[0])

    qc.rz(theta, q[0])

    qc.cx(q[1], q[0])

    qc.ry(-0.5 * pi, q[1])
    qc.rx(0.5 * pi, q[0])

    # measure_tasks = ['I', 'Z0', 'Z1', 'Z0Z1', 'X0X1', 'Y0Y1']

    if measure_task == 'X0X1':
        qc.ry(0.5 * pi, q[1])
        qc.ry(0.5 * pi, q[0])
    elif measure_task == 'Y0Y1':
        qc.rx(-0.5 * pi, q[1])
        qc.rx(-0.5 * pi, q[0])
    else:  # 'I', 'Z0', 'Z1', 'Z0Z1'
        pass

    qc.measure(q, c)

    # Compile and run the Quantum circuit on a simulator backend

    if IBM_BACKEND:
        job_sim = execute(qc, "ibmqx5", shots=SHOTS)
    else:
        job_sim = execute(qc, "local_qasm_simulator", shots=SHOTS)

    result = job_sim.result()

    if IBM_BACKEND:
        print('theta = ' + str(theta) + ', measure = ' + measure_task)
        print(result)

    counts = result.get_counts(qc)

    c = {}

    for key in ['00', '01', '10', '11']:
        if key in counts:
            c[key] = counts[key]
        else:
            c[key] = 0

    if measure_task == 'I':
        return (c['00'] + c['01'] + c['10'] + c['11']) / SHOTS
    elif measure_task == 'Z0':
        return (c['00'] - c['01'] + c['10'] - c['11']) / SHOTS
    elif measure_task == 'Z1':
        return (c['00'] + c['01'] - c['10'] - c['11']) / SHOTS
    else:  # 'Z0Z1', 'X0X1', 'Y0Y1'
        return (c['00'] - c['01'] - c['10'] + c['11']) / SHOTS
