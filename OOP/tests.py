import pytest
from OOP import Matrix


def test__init__():
    m = Matrix(2, 2, [[1, 2], [2, 1]])
    assert m.lines == 2
    assert m.pillars == 2
    assert m.elements == [[1, 2], [2, 1]]


def test_input_matrix(mocker):
    pass

def test__str__():

