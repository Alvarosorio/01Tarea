import numpy as np

def planck(y):

    arg = np.tan(y)
    I = (arg**3 + arg**5) / (np.expm1(arg))

    return I
