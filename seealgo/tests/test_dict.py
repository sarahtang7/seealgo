"""
This file contains unit tests for
visualizations involving dictionary data structures.
"""

from seealgo import Dict


### UNIT TESTS


def test_initdict():
    """
    Test the visualization of an unchanged dictionary.
    """

    init_dict = {'key1': 'one', 'key2': 2, 'key3': 'three'}
    viz0 = Dict()
    viz0.see(None, init_dict)

    with open('dict1.gv', 'r', encoding='utf-8') as file:
        viz_contents = file.read()

    with open('outputFiles/initDictOutput.txt', 'r', encoding='utf-8') as true_file:
        true_contents = true_file.read()

    assert viz_contents == true_contents


def test_nesteddict():
    """
    Test the visualization of a nested dictionary.
    """

    nested_dict = {
        'key1': 'value1',
        'key2': {
            'nested_key1': 'nested_value1',
            'nested_key2': 'nested_value2',
        },
    }
    viz_nested = Dict()
    viz_nested.see(None, nested_dict)

    with open('dict2.gv', 'r', encoding='utf-8') as file:
        viz_contents = file.read()

    with open('outputFiles/nestedDictOutput.txt', 'r', encoding='utf-8') as true_file:
        true_contents = true_file.read()

    assert viz_contents == true_contents


def test_updatedict():
    """
    Test the visualization of adding
    a key:value pair to a dictionary.
    """

    dict1 = {'1': 1, '2': 4, '3': 9, '4':16}
    dict_new = {'5': 25, '6': 36, '7': 49}
    viz1 = Dict()

    def update_func(user_dict):
        user_dict.update(dict_new)
        return user_dict

    viz1.see(update_func, dict1)

    with open('dict3.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('dict4.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/updateDictOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/updateDictOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2


def test_popfromdict():
    """
    Test the visualization of removing
    a value from a dictionary.
    """

    dict2 = {'apple': 'red', 'banana': 'yellow', 'goldfish': 'gold', 'kiwi': 'green'}
    viz2 = Dict()

    def pop_func(user_dict):
        user_dict.pop('goldfish')
        return user_dict

    viz2.see(pop_func, dict2)

    with open('dict5.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('dict6.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/popDictOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/popDictOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert viz_contents1 == true_contents1
    assert viz_contents2 == true_contents2
