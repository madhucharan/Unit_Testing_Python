import pytest
from splitdata import *
import numpy as np
def test_split():
    data= np.array([[2,1],[3,4],[5,6],[9,8]])
    #we know that first half should be 2 rows and lets check it
    assert split(data)==2,"they are not equal and there is a mistake"

# def test_exc_split():
#     data=np.array([[3,4]])
#     with pytest.raises(ValueError) as exc_info:
#         split(data)