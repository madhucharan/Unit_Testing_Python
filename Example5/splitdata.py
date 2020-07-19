import numpy as np
import pytest

# data =  np.array([[11, 9]])

# def input():
#
#     with pytest.raises(ValueError):
#         split(data)

def split(data):
    no_rows = data.shape[0]
    firsthalf =no_rows-0.5*no_rows
    return firsthalf