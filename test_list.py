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


def test_insertToList():
    list2 = [100, 200, 400, 500, 600]
    viz2 = List()

    def insert_func(list):
        list.insert(2, 300)
        return list

    see_viz2 = viz2.see(insert_func, list2)

    with open('see4_.gv', 'r') as file:
        viz_contents1 = file.read()
    with open('see5_.gv', 'r') as file:
        viz_contents2 = file.read()

    with open('outputFiles/insertListOutput1.txt', 'r') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/insertListOutput2.txt', 'r') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_deleteFromList():
    list3 = [1, 2, 3, 3]
    viz3 = List()

    def delete_func(list):
        list.remove(3)
        return list

    see_viz3 = viz3.see(delete_func, list3)

    with open('see6_.gv', 'r') as file:
        viz_contents1 = file.read()
    with open('see7_.gv', 'r') as file:
        viz_contents2 = file.read()

    with open('outputFiles/deleteListOutput1.txt', 'r') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/deleteListOutput2.txt', 'r') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_setList():
    list4 = [2, 33, 333, 3333]
    viz4 = List()

    def set_func(list):
        list.__setitem__(0, 3)
        return list

    see_viz4 = viz4.see(set_func, list4)

    with open('see8_.gv', 'r') as file:
        viz_contents1 = file.read()
    with open('see9_.gv', 'r') as file:
        viz_contents2 = file.read()

    with open('outputFiles/setListOutput1.txt', 'r') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/setListOutput2.txt', 'r') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2

    
### INTEGRATION TEST

def test_listIntegration():
    list = [3, 53, 98, 2, 35, 46, 1]
    viz = List()

    def mix_func(list):
        list.remove(2)
        list.append(-10)
        list.insert(0, 0)
        list.__setitem__(4, 1000)
        return list
    
    see_viz = viz.see(mix_func, list)

    with open('see10_.gv', 'r') as file:
        viz_contents1 = file.read()
    with open('see11_.gv', 'r') as file:
        viz_contents2 = file.read()
    with open('see12_.gv', 'r') as file:
        viz_contents3 = file.read()
    with open('see13_.gv', 'r') as file:
        viz_contents4 = file.read()
    with open('see14_.gv', 'r') as file:
        viz_contents5 = file.read()

    with open('outputFiles/mixListOutput1.txt', 'r') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/mixListOutput2.txt', 'r') as true_file:
        true_contents2 = true_file.read()
    with open('outputFiles/mixListOutput3.txt', 'r') as true_file:
        true_contents3 = true_file.read()
    with open('outputFiles/mixListOutput4.txt', 'r') as true_file:
        true_contents4 = true_file.read()
    with open('outputFiles/mixListOutput5.txt', 'r') as true_file:
        true_contents5 = true_file.read()
    
    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2
    assert viz_contents3 == true_contents3
    assert viz_contents4 == true_contents4
    assert viz_contents5 == true_contents5