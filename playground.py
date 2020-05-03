import qiskit as qk
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector

from sklearn.preprocessing import LabelBinarizer
from math import sqrt, pi
import numpy as np
import cv2

info = "rohan"
org = cv2.imread('./img/bruh.jpg')
img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
row1 = img[0]


# testing with dummy row
r = [20,22,23,43,43,123,7,8,9]
# one-hot encode them -> convert them to binary vectors
lb = LabelBinarizer()
r_oneHot = lb.fit_transform(r)

# qbits = []
# # create qbits
circuits = []
for vector in r_oneHot:
    qBitNum = 3
    qc = QuantumCircuit(qBitNum) # for vector of size 2^3=8
    initial_state = vector   # Define initial_state as |1>. sum of amplitudes = 1, has to be power of 2
    qc.initialize(initial_state, list(range(qBitNum))) # Apply initialisation operation to the 0th qubit
    # qc.draw()
    circuits.append(qc)



backend = Aer.get_backend('statevector_simulator')
def getVector(qc):
    result = execute(qc,backend).result()
    out_state = result.get_statevector()
    # print(out_state)
    vector = [int(x.real) for x in out_state]
    return vector

retrievedVectors=[]
for circuit in circuits:
    retrievedVectors.append(getVector(circuit))
retrievedVectors = np.array(retrievedVectors) # convert to numpy array
print(retrievedVectors)
lb.inverse_transform(retrievedVectors)