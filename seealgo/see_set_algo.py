"""

This module contains the functionality to visualize a set
data structure as it changes throughout a function.

This involves the following classes:

* `TrackedSet(set)`: detects changes made to a given set
  data structure and triggers creation of a new visualization for each change.

* `Set`: uses graphviz to construct a visualization of a set.

"""
from graphviz import Digraph

class TrackedSet(set):
    """
    Tracks changes to a set data structure and triggers creation of new visualization

    Args:
        set: the set data structure to track
    """

    def add(self, value):
        """
        Adds an element to the set and invokes a new visualization

        Args:
            value (Any): element to be added to the set
        """
        super().add(value)
        Set.create_viz(self, self, value)


    def remove(self, value):
        """
        Removes an element from the set and invokes a new visualization

        Args:
            value (Any): element to be removed from the set

        Raises:
            KeyError: If the element to be removed is not in the set.
        """
        super().remove(value)
        Set.create_viz(self, self)


    def clear(self):
        """
        Clears the set and invokes a new visualization
        """
        super().clear()
        Set.create_viz(self, self)


    def update(self, values):
        """
        Adds multiple elements to the set and invokes a new visualization

        Args:
            values (iterable): iterable of elements to be added to the set
        """
        super().update(values)
        Set.create_viz(self, self)


class Set:
    """
    Create graphviz visualization for set data structure
    """

    filenum = 1

    def see(self, func, data):
        """
        Creates a visualization for the initial set and starts tracking
        a given set as it changes throughout a given function.

        Args:
            func (function): function that the set is being altered through
            data (set): set to track
        """
        Set.create_viz(self, data)
        data = TrackedSet(data)
        if func is not None:
            func(data)


    def create_viz(self, data, value=None):
        """
        Creates and renders a visualization of the set using graphviz

        Args:
            data (set): set that is being visualized
            value (Any): optional value to highlight in the visualization
        """
        di_graph = Digraph('Set', filename=f'set{Set.filenum}.gv')
        Set.filenum += 1
        di_graph.attr(rankdir='LR')

        with di_graph.subgraph(name='cluster_Set') as subgraph:
            subgraph.attr(label='Set')
            subgraph.attr(style='filled')
            subgraph.attr(color='lightgrey')
            subgraph.node_attr.update(style='filled', color='white')

            # Create nodes for each element in the set
            for val in sorted(data):
                if val == value:
                    subgraph.node(str(val), label=str(val), style='filled', color='green')
                else:
                    subgraph.node(str(val), label=str(val))

        # Render the graph to a file
        di_graph.view()
