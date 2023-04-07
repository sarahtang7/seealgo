"""
This file contains visualizes a tree data structure
as it changes throughout a function.
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
        Insert a child node into a binary search tree.
        """
        dict_form = tracked_tree_to_dict(self)
        added = add_to_bst(dict_form, child)
        print(added)

        new_tree = nested_dict_to_tracked_tree(added)
        self.label = new_tree.label
        self.children = new_tree.children


    def remove(self, val):
        """
        Remove a child node from the tree.
        """
        dict_form = tracked_tree_to_dict(self)
        removed = remove_node(dict_form, val)

        new_tree = nested_dict_to_tracked_tree(removed)
        self.label = new_tree.label
        self.children = new_tree.children


def nested_dict_to_tracked_tree(tree_dict):
    """
    Convert from nested dictionary (user input form) to
    a nested TrackedTree object form.
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
    Convert from TrackedTree object form to
    nested dictionary form.
    """

    if not tree.children:
        return {tree.label: None}

    children = {}

    for child in tree.children:
        children.update(tracked_tree_to_dict(child))

    return {tree.label: children}


def add_to_bst(bst, value):
    """
    Add a leaf value to a binary search tree in
    nested dictionary form.
    """

    if not bst:  # If the tree is empty, create a new node for the value
        return {value: {}}

    bst_value = int(list(bst.keys())[0])

    if value < bst_value:  # If value is less than the current node, go left
        left_key = list(bst.keys())[0]
        bst[left_key] = add_to_bst(bst[left_key], value)

    elif value > bst_value:  # If value is greater than the current node, go right
        if value > bst_value:
            right_key = list(bst.keys())[0]
        else:
            right_key = list(bst.keys())[1]
        bst[right_key] = add_to_bst(bst[right_key], value)

    return bst


def remove_node(root, val):
    """
    Remove val from a tree in nested
    dictionary form.
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
    Tracks changes to a tree data structure.
    """

    def __init__(self, label, children=None):
        super().__init__(label, children)
        self.size = self.get_size()
        self.newest_nodes = []


    def add_child(self, child_val):
        """
        Add a child leaf node to a binary
        search tree.
        """

        super().insert(child_val)
        Tree.create_viz(self)


    def remove_node(self, child):
        """
        Remove a node and its children (if applicable)
        from a tree.
        """

        super().remove(child)
        #self.children.remove(child)
        Tree.create_viz(self)


    def check_size(self):
        """
        Create a new visualization when
        a change is made to the tree.
        """

        if self.get_size() != self.size:
            self.size = self.get_size()
            print("Tree Changed")
            Tree.create_viz(self)


    def get_size(self):
        """
        Calculate the size of the tree.
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
        Start tracking a given tree as
        it changes throughout a given function.
        """
        tree = nested_dict_to_tracked_tree(tree)
        Tree.create_viz(tree)
        tree = TrackedTree(tree.label, [TrackedTree(c.label, c.children) for c in tree.children])
        if func is not None:
            func(tree)


    @staticmethod
    def create_viz(tree):
        """
        Render graphviz visualization.
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
        Create a graphviz node for the given tree node.
        """

        di_graph.node(str(id(tree)), label=str(tree.label))

        if parent is not None:
            di_graph.edge(str(id(parent)), str(id(tree)))

        for child in tree.children:
            Tree.create_node(di_graph, child, tree)
