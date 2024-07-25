import pytest
import hypot.source as source

# test sqrt function

def test_sqrt4():
    input = 4
    e_output = 2
    output = source.sqrt(input)
    assert output == e_output


def test_sqrt9():
    input = 9
    e_output = 3
    output = source.sqrt(input)
    assert output == e_output
    
    
 # test hypot function
 
def test_hypot345():
    in_a = 3
    in_b = 4
    e_output = 5
    output = source.hypot(in_a, in_b)
    assert output == e_output

def test_hypot304050():
    in_a = 30
    in_b = 40
    e_output = 50
    output = source.hypot(in_a, in_b)
    assert output == e_output