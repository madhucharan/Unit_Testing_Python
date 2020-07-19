
from make_list import *
def test_formlist():
    statement = "This is pytest"
    assert formlist(statement)==['This','is','pytest']

def test_unique():
    statement = "This is pytest example.Check This"
    assert list(set(formlist(statement))).sort()==['This ' ,'is','pytest','example.Check'].sort()

if __name__ == "__main__":
    main()