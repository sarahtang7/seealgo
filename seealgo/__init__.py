"""
Set up relative imports.
"""

from seealgo.see_tree_algo import Tree
from .see_list_algo import List

myList = List()
myTree = Tree()

__all__ = [
    'List', 'Tree'
]
