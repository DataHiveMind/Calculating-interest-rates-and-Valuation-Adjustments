"""
Simluation of, E(W(t)|F(s)) = W(s)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = 10
s = 5
NoofPaths = 1000
NoofSteps = 10

def martingaleA():
    w_t = np.random.normal(0.0, pow(t, 0.5), [NoofPaths,1])
    e_w_t = np.mean(w_t)
    print("mean value equals to: %.2f while the expected value is W(0) = %0.2f" %(e_w_t,0.0))

if __name__ == "__main__":
    martingaleA()