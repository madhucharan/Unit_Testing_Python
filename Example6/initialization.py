import numpy as np

def initializing(n_p,n_i,n_o):

    #let ni= current layer size
    #let npp=previous layer size
    #let no=size of output layer which is fed into next layer
    W1 = np.random.randn(n_i, n_p) * 0.01
    b1 = np.zeros((n_i, 1))
    W2 = np.random.randn(n_o, n_i) * 0.01
    b2 = np.zeros((n_o, 1))
    return W1,W2,b1,b2