"""
Set up relative imports.
"""

from .see_list_algo import List
from seealgo.see_tree_algo import Tree

myList = List()
myTree = Tree()

__all__ = [
    'List', 'Tree'
]
