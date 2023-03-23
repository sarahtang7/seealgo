"""
This file contains unit and integration tests for
visualizations involving only list data structures.
"""

from seealgo import List


### UNIT TESTS

def test_initlist():
    """
    Test the visualization of an unchanged list.
    """

    init_list = [2, 4, 6, 8, 10, 12, 14]
    viz0 = List()
    viz0.see(None, init_list)

    with open('see1.gv', 'r', encoding='utf-8') as file:
        viz_contents = file.read()

    with open('outputFiles/initListOutput.txt', 'r', encoding='utf-8') as true_file:
        true_contents = true_file.read()

    assert viz_contents == true_contents


def test_appendlist():
    """
    Test the visualization of appending
    a value to a list.
    """

    list1 = [1, 2, 3, 4]
    viz1 = List()

    def append_func(lst):
        lst.append(5)
        return lst

    viz1.see(append_func, list1)

    with open('see2.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('see3.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/appendListOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/appendListOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_inserttolist():
    """
    Test the visualization of inserting
    a value at an index within the list.
    """

    list2 = [100, 200, 400, 500, 600]
    viz2 = List()

    def insert_func(lst):
        lst.insert(2, 300)
        return lst

    viz2.see(insert_func, list2)

    with open('see4.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('see5.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/insertListOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/insertListOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_deletefromlist():
    """
    Test the visualization of deleting
    a value from the list.
    """

    list3 = [1, 2, 3, 3]
    viz3 = List()

    def delete_func(lst):
        lst.remove(3)
        return lst

    viz3.see(delete_func, list3)

    with open('see6.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('see7.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/deleteListOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/deleteListOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_setlist():
    """
    Test the visualization of assigning
    another value to an element in the list.
    """

    list4 = [2, 33, 333, 3333]
    viz4 = List()

    def set_func(lst):
        lst[0] = 3
        return lst

    viz4.see(set_func, list4)

    with open('see8.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('see9.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/setListOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/setListOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


### INTEGRATION TEST

def test_listintegration():
    """
    Test the visualization of various operations
    on the same list.
    """

    lst = [3, 53, 98, 2, 35, 46, 1]
    viz = List()

    def mix_func(lst):
        lst.remove(2)
        lst.append(-10)
        lst.insert(0, 0)
        lst[4] = 1000
        return lst

    viz.see(mix_func, lst)

    with open('see10.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('see11.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()
    with open('see12.gv', 'r', encoding='utf-8') as file:
        viz_contents3 = file.read()
    with open('see13.gv', 'r', encoding='utf-8') as file:
        viz_contents4 = file.read()
    with open('see14.gv', 'r', encoding='utf-8') as file:
        viz_contents5 = file.read()

    with open('outputFiles/mixListOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/mixListOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()
    with open('outputFiles/mixListOutput3.txt', 'r', encoding='utf-8') as true_file:
        true_contents3 = true_file.read()
    with open('outputFiles/mixListOutput4.txt', 'r', encoding='utf-8') as true_file:
        true_contents4 = true_file.read()
    with open('outputFiles/mixListOutput5.txt', 'r', encoding='utf-8') as true_file:
        true_contents5 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2
    assert viz_contents3 == true_contents3
    assert viz_contents4 == true_contents4
    assert viz_contents5 == true_contents5
