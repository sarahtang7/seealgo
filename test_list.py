import pytest

from graphviz import Digraph
from typing import List
from seealgo.seeListAlgo import List


### UNIT TESTS

def test_initList():
    init_list = [2, 4, 6, 8, 10, 12, 14]
    viz0 = List()
    see_viz = viz0.see(None, init_list)

    with open('see1_.gv', 'r') as file:
        viz_contents = file.read()

    with open('outputFiles/initListOutput.txt', 'r') as true_file:
        true_contents = true_file.read()

    assert viz_contents == true_contents
