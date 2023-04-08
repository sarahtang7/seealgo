"""

This module contains the functionality to visualize a binary
search tree data structure as nodes are inserted and removed.

This involves the following classes:

* `TreeDS`: defines a custom tree data structure

* `TrackedTree(TreeDS)`: detects changes made to a given TreeDS data structure and
  triggers creation of a new visualization for each change

* `Tree`: uses graphviz to construct a node-edge visualization of the tree

"""


from graphviz import Digraph

class TreeDS:
    """
    Define a custom tree data structure.
    """
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []


    def insert(self, child):
        """
        Inserts a leaf node into a binary search tree.

        Args:
            child (Any): value of leaf node to be inserted
        """
        dict_form = tracked_tree_to_dict(self)
        added = add_to_bst(dict_form, child)

        new_tree = nested_dict_to_tracked_tree(added)
        self.label = new_tree.label
        self.children = new_tree.children


    def remove(self, val):
        """
        Removes a child node from the binary search tree.

        Args:
            val (Any): value of the node to be removed
        """
        dict_form = tracked_tree_to_dict(self)
        removed = remove_node(dict_form, val)

        new_tree = nested_dict_to_tracked_tree(removed)
        self.label = new_tree.label
        self.children = new_tree.children


def nested_dict_to_tracked_tree(tree_dict):
    """
    Helper method that converts a nested dictionary (the user input form of the tree)
    to a nested TrackedTree object form.

    Args:
        tree_dict (dict): nested dictionary to be converted to TrackedTree object form

    Returns:
        The nested TrackedTree object form of the input dictionary.
    """
    def _recurse(node_dict):

        label, children_dict = next(iter(node_dict.items()))
        children = None

        if children_dict:
            children = [_recurse({k: v}) for k, v in children_dict.items()]

        return TrackedTree(label, children)

    return _recurse(tree_dict)


def tracked_tree_to_dict(tree):
    """
    Helper method that converts a nested TrackedTree object to a nested dictionary.

    Args:
        tree (nested seealgo.see_tree_algo.TrackedTree): TrackedTree object form
        to be converted to nested dictionary form

    Returns:
        The nested dictionary form of the input nested TrackedTree object.
    """
    if not tree.children:
        return {tree.label: None}

    children = {}

    for child in tree.children:
        children.update(tracked_tree_to_dict(child))

    return {tree.label: children}


def add_to_bst(bst, value):
    """
    Helper method that recursively adds a new leaf node with the given value
    to its correct place in a binary search tree represented as a nested dictionary.

    Args:
        bst (dict): the binary search tree in nested dictionary form
        value (Any): The value to be inserted as a new node.

    Returns:
        The updated binary search tree in nested dictionary form with the specified node added.
    """
    if not bst:  # if the tree is empty, create a new node for the value
        return {value: {}}

    bst_value = int(list(bst.keys())[0])

    if value < bst_value:  # if value is less than the current node, go left
        left_key = list(bst.keys())[0]
        bst[left_key] = add_to_bst(bst[left_key], value)

    elif value > bst_value:  # if value is greater than the current node, go right
        if value > bst_value:
            right_key = list(bst.keys())[0]
        else:
            right_key = list(bst.keys())[1]
        bst[right_key] = add_to_bst(bst[right_key], value)

    return bst


def remove_node(root, val):
    """
    Helper method that recursively removes the first node with a given value from a tree
    in nested dictionary form.

    Args:
        root (dict): the root of the tree to remove a node from
        val (Any): the value of the node to be removed

    Returns:
        The updated binary search tree in nested dictionary form with the specified node removed.
        If the value is not found in the tree, this method will return the original tree.
    """
    val = str(val)
    if root is None:
        return None

    root_copy = dict(root)

    if isinstance(root, dict):

        for k, value in root_copy.items():
            if k == val:
                del root[k]

            else:
                remove_node(value, val)

    elif isinstance(root, list):
        for item in root:
            remove_node(item, val)

    return root


class TrackedTree(TreeDS):
    """
    Tracks changes to a TreeDS data structure and triggers creation of new visualization

    Args:
        TreeDS (seealgo.see_tree_algo.TreeDS): the tree data structure to track
    """

    def __init__(self, label, children=None):
        """
        Initializes a TrackedTree object (similar to a node) and sets the size attribute
        to the size of the object.

        Args:
            label (str): represents the value of the TrackedTree object
            children (:obj:`TrackedTree`, optional): child TrackedTree objects of the current
                object. The default value is None.
        """
        super().__init__(label, children)
        self.size = self.get_size()


    def add_child(self, val):
        """
        Adds a leaf node with the specified value to the current binary search tree object.

        Args:
            val (Any): the value to be added to the binary search tree
        """
        super().insert(val)
        Tree.create_viz(self)


    def remove_node(self, to_remove):
        """
        Removes a node and its children (if applicable) from a binary search tree.

        Args:
            to_remove (Any): value of the node to remove from the tree
        """
        super().remove(to_remove)
        Tree.create_viz(self)


    def check_size(self):
        """
        Checks if there has been a change in the size of the tree and creates a new visualization
        if there has been a change.
        """
        if self.get_size() != self.size:
            self.size = self.get_size()
            print("Tree Changed")
            Tree.create_viz(self)


    def get_size(self):
        """
        Calculates the size of the tree based on the number of nodes in the tree.
        """
        size = 1
        for child in self.children:
            size += child.get_size()
        return size


class Tree:
    """
    Create graphviz visualization for tree data structure.
    """

    filenum = 1

    @staticmethod
    def see(func, tree):
        """
        Creates a visualization for the initial tree and starts tracking
        the tree as it changes throughout a given function.

        Args:
            func (function): function that the tree is being altered through
            tree (dict): tree to track in nested dictionary form
        """
        tree = nested_dict_to_tracked_tree(tree)
        Tree.create_viz(tree)
        tree = TrackedTree(tree.label, [TrackedTree(c.label, c.children) for c in tree.children])
        if func is not None:
            func(tree)


    @staticmethod
    def create_viz(tree):
        """
        Creates and renders a visualization of the tree using graphviz

        Args:
            tree (seealgo.see_tree_algo.TrackedTree): tree to create visualization of
        """

        di_graph = Digraph('Tree', filename=f'tree{Tree.filenum}.gv')
        Tree.filenum += 1

        # Create nodes for each element in the tree
        Tree.create_node(di_graph, tree)

        # Render the graph to a file
        di_graph.view()


    @staticmethod
    def create_node(di_graph, tree, parent=None):
        """
        Creates a visualization of a single node in a tree using Graphviz, and adds
        it to the given directed graph.

        Args:
            di_graph (graphviz.dot.Digraph): a directed graph to add the node visualization to
            tree (seealgo.see_tree_algo.TrackedTree): tree to create visualization of
            parent (seealgo.see_tree_algo.TrackedTree, optional): the parent of the current node.
                Defaults to None
        """
        di_graph.node(str(id(tree)), label=str(tree.label))

        if parent is not None:
            di_graph.edge(str(id(parent)), str(id(tree)))

        for child in tree.children:
            Tree.create_node(di_graph, child, tree)
