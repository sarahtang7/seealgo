"""
This file contains unit tests for
visualizations involving set data structures.
"""

from seealgo import Set


### UNIT TESTS

def test_initset():
    """
    Test the visualization of an unchanged set.
    """

    init_set = {1,2,3,4,5,6,7}
    viz0 = Set()
    viz0.see(None, init_set)

    with open('set1.gv', 'r', encoding='utf-8') as file:
        viz_contents = file.read()

    with open('outputFiles/initSetOutput.txt', 'r', encoding='utf-8') as true_file:
        true_contents = true_file.read()

    assert viz_contents == true_contents


def test_addtoset():
    """
    Test the visualization of adding
    a value to a set.
    """

    set1 = {7, 71, 227}
    viz1 = Set()

    def add_func(user_set):
        user_set.add(353)
        return user_set

    viz1.see(add_func, set1)

    with open('set2.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('set3.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/addSetOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/addSetOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_removefromset():
    """
    Test the visualization of removing
    a value from a set.
    """

    set2 = {2,4,5,6,8}
    viz2 = Set()

    def remove_func(user_set):
        user_set.remove(5)
        return user_set

    viz2.see(remove_func, set2)

    with open('set4.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('set5.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/removeSetOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/removeSetOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_clearset():
    """
    Test the visualization of clearing a set.
    """

    set3 = {3,89,12}
    viz3 = Set()

    def clear_func(user_set):
        user_set.clear()
        return user_set

    viz3.see(clear_func, set3)

    with open('set6.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('set7.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/clearSetOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/clearSetOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_updateset():
    """
    Test the visualization of updating a set.
    """

    set4 = {1,2,3,7,8,9}
    viz4 = Set()

    def update_func(user_set):
        list_to_add = [4,5,6]
        user_set.update(list_to_add)
        return user_set

    viz4.see(update_func, set4)

    with open('set8.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('set9.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/updateSetOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/updateSetOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2
