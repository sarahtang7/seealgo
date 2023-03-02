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


def test_appendList():
    list1 = [1, 2, 3, 4]
    viz1 = List()

    def append_func(list):
        list.append(5)
        return list

    see_viz1 = viz1.see(append_func, list1)

    with open('see2_.gv', 'r') as file:
        viz_contents1 = file.read()
    with open('see3_.gv', 'r') as file:
        viz_contents2 = file.read()

    with open('outputFiles/appendListOutput1.txt', 'r') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/appendListOutput2.txt', 'r') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2