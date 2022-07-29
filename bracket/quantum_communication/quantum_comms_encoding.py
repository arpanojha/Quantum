from braket import *

from braket.circuits import Circuit, Gate, Observable
from braket.devices import LocalSimulator
from braket.circuits import circuit
import matplotlib.pyplot as plt

device = LocalSimulator("default")

encoding_dictionary = {
    '00': Circuit().i(0),
    '01': Circuit().x(0),
    '10': Circuit().z(0),
    '11': Circuit().x(0).z(0),
}
for k in encoding_dictionary.keys():
    circuit = Circuit()
    circuit = circuit.h(0).cnot(0,1)+encoding_dictionary[k]
    result = device.run(circuit, shots=1000).result()
    counts = result.measurement_counts
    print(circuit)
