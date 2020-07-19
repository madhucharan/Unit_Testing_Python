import numpy as np
from initialization import *
def test_shape():
    W1,W2,b1,b2= initializing(5,3,2)
    assert (W1.shape == (3,5))
    assert (b1.shape == (3, 1))
    assert (W2.shape == (2, 3))
    assert (b2.shape == (2, 1))