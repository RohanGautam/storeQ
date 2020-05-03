import qiskit as qk
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector

from sklearn.preprocessing import LabelBinarizer
from math import sqrt, pi
import numpy as np
import cv2
import math
from tqdm import tqdm
# custom : 
from customLabelBinarizer import CustomLabelBinarizer
import imutils

info = "rohan"
org = cv2.imread('/home/rohan/Desktop/Python_files/quantumExploring/img/puppy.png')
img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
img = imutils.resize(img, width=100)
row1 = img[0]
# cv2.imshow("image", img)
# cv2.waitKey(0)

def closestPowerOfTwo(n):
    return 2**math.ceil(math.log(n)/math.log(2))

def highestPowerOfTwo(img):
    '''highest power of two amongst all rows'''
    maxVal = max([closestPowerOfTwo(len(list(set(row)))) for row in img])
    return (maxVal, int(math.log(maxVal,2)))

def removePadding(matrix):
    '''remove padded zeroes from the matrix to give the original LabelBinarizer binary vectors'''
    # calculate index of the '1' that has the furthest/max index. 
    # This will be the boundary, beyond which we will discard the columns (zeroes)
    boundary = max([list(l).index(1) for l in matrix]) # index, begins from 0
    print(boundary)
    return matrix[:, :boundary+1] # return sliced matrix

powerVal, exponent = highestPowerOfTwo(img)

lb_binarizers = []
rows_circuits = []
def startUpload ():
    print('[INFO] One-Hot encoding matrix rows')
    for row in tqdm(img) :
        # one-hot encode them -> convert them to binary vectors
        # why? because sum of amplitudes we pass should be = 1
        lb = CustomLabelBinarizer()
        r_oneHot = lb.fit_transform(row)
        lb_binarizers.append(lb)
        # pad extra with zeroes, so that row length is the max power of 2
        padNum = powerVal-r_oneHot.shape[1]
        r_padded = np.hstack((r_oneHot, np.zeros((r_oneHot.shape[0], padNum), dtype=r_oneHot.dtype)))

        # qbits = []
        # # create qbits
        circuits = []
        for vector in r_padded:
            qBitNum = exponent
            qc = QuantumCircuit(qBitNum) 
            initial_state = vector   # Define initial_state as |1>. sum of amplitudes = 1, has to be power of 2
            qc.initialize(initial_state, list(range(qBitNum))) # Apply initialisation operation to the 0th qubit
            # qc.draw()
            circuits.append(qc)
        rows_circuits.append(circuits)



backend = Aer.get_backend('statevector_simulator')
def getOneHotVector(qc):
    result = execute(qc,backend).result()
    out_state = result.get_statevector()
    # print(out_state)
    vector = [int(x.real) for x in out_state]
    return vector


def startDownload():
    finalImage = []
    for i in tqdm(range(len(rows_circuits))):
        row_circuit = rows_circuits[i]
        retrievedVectors=[]
        for circuit in row_circuit:
            retrievedVectors.append(getOneHotVector(circuit))
        retrievedVectors = np.array(retrievedVectors) # convert to numpy array
        retrievedVectors = removePadding(retrievedVectors)
        # set the lb_binarizer to lb_binarizers[-1] to make it seem like it was hazy(error before)
        row = lb_binarizers[i].inverse_transform(retrievedVectors)# the final vector
        print(row.shape)
        finalImage.append(row)

    finalImage = np.array(finalImage)
    ## show it : 
    cv2.imshow("Reconstructed image", finalImage)
    cv2.waitKey(0)

# startUpload()
# startDownload()