from braket import *

from braket.circuits import Circuit, Gate, Observable
from braket.devices import LocalSimulator
from braket.circuits import circuit
import matplotlib.pyplot as plt
device = LocalSimulator("default")
circuit = Circuit().h(0)
def quantum_seed(n):
    s = ''
    for i in range(n):
        result = device.run(circuit, shots=1).result()
        counts = result.measurement_counts
        s+=list(counts.keys())[0]
    return hex(int(s, 2))

print(quantum_seed(4))