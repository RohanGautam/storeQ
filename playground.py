import qiskit as qk
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi
from sklearn.preprocessing import LabelBinarizer
import cv2

info = "rohan"
org = cv2.imread('./img/bruh.jpg')
img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
row1 = img[0]


# testing with dummy row
r = [20,22,23,43,43,123,7,8]
# one-hot encode them -> convert them to binary vectors
lb = LabelBinarizer()
lb.fit_transform(r)

qbits = []
# create qbits



qc = QuantumCircuit(2)
initial_state = [0,1,0,0]   # Define initial_state as |1>. sum of amplitudes = 1, has to be power of 2
qc.initialize(initial_state, [0,1]) # Apply initialisation operation to the 0th qubit
qc.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qc,backend).result()
out_state = result.get_statevector()
print(out_state)
# out_state.real is the real number part

# Creating Qubits
q = qk.QuantumRegister(2)
# Creating Classical Bits
c = qk.ClassicalRegister(2)
