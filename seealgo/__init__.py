"""
Set up relative imports.
"""

from seealgo.see_tree_algo import Tree
from seealgo.see_set_algo import Set
from seealgo.see_dict_algo import Dict
from .see_list_algo import List

myList = List()
myTree = Tree()
mySet = Set()
myDict = Dict()

__all__ = [
    'List', 'Tree', 'Set', 'Dict'
]
