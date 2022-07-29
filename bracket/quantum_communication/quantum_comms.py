from braket import *

from braket.circuits import Circuit, Gate, Observable
from braket.devices import LocalSimulator
from braket.circuits import circuit
import matplotlib.pyplot as plt

device = LocalSimulator("default")
circuit = Circuit()

circuit.h(0).cnot(0,1)
result = device.run(circuit, shots=1000).result()
counts = result.measurement_counts
# sns.set_theme(style="white")
plt.bar(counts.keys(), counts.values(), alpha=0.5, color='pink')
plt.title(print(circuit))
plt.xlabel('bitstrings')
plt.ylabel('counts')
plt.show()