"""
This file contains visualizes a list data structure
as it changes throughout a function.
"""

from graphviz import Digraph

class TrackedArray(list):
    """
    Tracks changes to a list data structure.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.length = len(self)

    def append(self, value):
        super().append(value)
        self.check_length(self.length, True)

    def insert(self, index, value):
        super().insert(index, value)
        self.check_length(index, True)

    def remove(self, value):
        super().remove(value)
        self.check_length(None, True)

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        self.check_length(index, True)

    def check_length(self, index, invoke):
        """
        Create a new visualization when
        a change is made to the list.
        """

        if len(self) != self.length or invoke:
            self.length = len(self)
            print("Array Changed")
            List.create_viz(self, self, index)


class List:
    """
    Create graphviz visualization
    for list data structure.
    """

    filenum = 1

    def see(self, func, data):
        """
        Start tracking a given list as
        it changes throughout a given function.
        """

        List.create_viz(self, data, None)
        data = TrackedArray(data)
        if func is not None:
            func(data)

    def create_viz(self, data, index):
        """
        Render graphviz visualization.
        """

        di_graph = Digraph('List', filename=f'see{List.filenum}.gv')
        List.filenum += 1
        di_graph.attr(rankdir='LR')

        # Create nodes for each element in the list
        for i, val in enumerate(data):
            node_style = 'filled' if i == index else ''
            node_fillcolor = 'green' if i == index else ''
            di_graph.node(str(i), label=str(val), style=node_style, fillcolor=node_fillcolor)

        # Create edges between adjacent nodes
        for i in range(len(data) - 1):
            di_graph.edge(str(i), str(i + 1))

        # Render the graph to a file
        di_graph.view()
