from divide import *
import pytest
def test_div():
    with pytest.raises(ZeroDivisionError):
        div(2)



