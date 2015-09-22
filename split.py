import numpy as np

def split(T):

    n = T.shape
    F = np.zeros((1, n[0]))
    W = np.zeros((1, n[0]))

    for i in range(0, n[0]):
        F[0,i] = T[i][1]
        W[0,i] = T[i][0]


    K = np.append(W, F, axis=0)
    return K
