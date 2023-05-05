"""

This module contains the functionality to visualize a list
data structure as it changes throughout a function.

This involves the following classes:

* `TrackedArray(list)`: detects changes made to a given list
  data structure and triggers creation of a new visualization for each change.

* `List`: uses graphviz to construct a node-edge visualization of a list.

"""

from graphviz import Digraph

class TrackedArray(list):
    """
    Tracks changes to a list data structure and triggers creation of new visualization

    Args:
        list: the list data structure to track
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a list object and sets the length attribute to the length of the object

        Args:
            *args: Non-keyworded variable length argument list.
            **kwargs: Keyworded variable length argument list.
        """
        super().__init__(*args, **kwargs)
        self.length = len(self)


    def append(self, value):
        """
        Appends an element to the end of the list and checks the length of the list

        Args:
            value (Any): element to be appended to the list
        """
        super().append(value)
        self.check_length(self.length, True)


    def insert(self, index, value):
        """
        Inserts an element at a specified position and checks the length of the list

        Args:
            index (int >= 0): position at which the element is to be inserted
            value (Any): value of element to be inserted at the specified index
        """
        super().insert(index, value)
        self.check_length(index, True)


    def remove(self, value):
        """
        Removes the first occurrence of a value from the list and checks the length of the list

        Args:
            value (Any): value to be removed from the list
        """
        super().remove(value)
        self.check_length(None, True)


    def __setitem__(self, index, value):
        """
        Sets the value of an item at a specified index and checks the length of the list

        Args:
            index (int): index of the element to be set
            value (Any): value to be set at the specified index
        """
        super().__setitem__(index, value)
        self.check_length(index, True)


    def check_length(self, index, invoke):
        """
        Checks for change in the length of the list and triggers creation
        of a new visualization if the list length has changed.

        Args:
            index (int): index of the element that has changed
            invoke (boolean): indicates whether the visualization should be created
        """
        if len(self) != self.length or invoke:
            self.length = len(self)
            print("Array Changed")
            List.create_viz(self, self, index)


class List:
    """
    Create graphviz visualization for list data structure
    """

    filenum = 1

    def see(self, func, data):
        """
        Creates a visualization for the initial list and starts tracking
        a given list as it changes throughout a given function.

        Args:
            func (function): function that the list is being altered through
            data (list): list to track
        """
        List.create_viz(self, data, None)
        data = TrackedArray(data)
        if func is not None:
            func(data)


    def create_viz(self, data, index):
        """
        Creates and renders a visualization of the list using graphviz

        Args:
            data (list): list that is being visualized
            index (int): index of the element that has been changed
        """
        di_graph = Digraph('List', filename=f'see{List.filenum}.gv')
        List.filenum += 1
        di_graph.attr(rankdir='LR')

        # Create nodes for each element in the list
        for i, val in enumerate(data):
            node_style = 'filled' if i == index else ''
            node_fillcolor = 'green' if i == index else ''
            label = f"[{i}]\n\n{val}"
            di_graph.node(str(i), label=label, style=node_style, fillcolor=node_fillcolor)

        # Create edges between adjacent nodes
        for i in range(len(data) - 1):
            di_graph.edge(str(i), str(i + 1))

        # Render the graph to a file
        di_graph.view()
