"""
This file contains unit and integration tests for
visualizations involving only tree data structures.
"""

from seealgo import Tree

### UNIT TESTS

def test_init_tree():
    """
    Test the visualization of an unchanged tree.
    """

    tree = {'A': {
            'B': {
                'D': None,
                'E': None
            },
            'C': {
                'F': None,
                'G': {
                    'H': None,
                    'I': None
                }
            }
    }}

    my_tree = Tree()
    my_tree.see(None, tree)

    with open('tree1.gv', 'r', encoding='utf-8') as file:
        viz_contents = file.read()

    with open('outputFiles/initTreeOutput.txt', 'r', encoding='utf-8') as true_file:
        true_contents = true_file.read()

    assert len(viz_contents) == len(true_contents)


def test_insert_tree():
    """
    Test the visualization of inserting into a binary search tree.
    """

    tree = {
        '8': {
            '3': {
                '1': None,
                '6': None
            },
            '10': None
        }
    }

    viz1 = Tree()

    def insert_func(init_tree):
        init_tree.add_child(2)
        return init_tree

    viz1.see(insert_func, tree)

    with open('tree2.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('tree3.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/addTreeOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/addTreeOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert len(viz_contents1) == len(true_contents1)
    assert len(viz_contents2) == len(true_contents2)


def test_remove_node():
    """
    Test the visualization of removing a node from a binary search tree.
    """

    tree = {
        '5': {
            '2': {
                '-4': None,
                '3': None
            },
            '18': None
        }
    }

    viz2 = Tree()

    def insert_func(init_tree):
        init_tree.remove_node(18)
        return init_tree

    viz2.see(insert_func, tree)

    with open('tree4.gv', 'r', encoding='utf-8') as file:
        viz_contents1 = file.read()
    with open('tree5.gv', 'r', encoding='utf-8') as file:
        viz_contents2 = file.read()

    with open('outputFiles/deleteTreeOutput1.txt', 'r', encoding='utf-8') as true_file:
        true_contents1 = true_file.read()
    with open('outputFiles/deleteTreeOutput2.txt', 'r', encoding='utf-8') as true_file:
        true_contents2 = true_file.read()

    assert len(viz_contents1) == len(true_contents1)
    assert len(viz_contents2) == len(true_contents2)
