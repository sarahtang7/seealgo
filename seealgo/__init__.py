"""
Set up relative imports.
"""

from seealgo.see_tree_algo import Tree
from seealgo.see_set_algo import Set
from .see_list_algo import List

myList = List()
myTree = Tree()
mySet = Set()

__all__ = [
    'List', 'Tree', 'Set'
]
