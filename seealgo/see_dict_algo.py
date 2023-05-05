"""
This module contains the functionality to visualize a dictionary
data structure as it changes throughout a function.
This involves the following classes:
* `TrackedDict(dict)`: detects changes made to a given dictionary
  data structure and triggers creation of a new visualization for each change.
* `Dict`: uses graphviz to construct a visualization of the dictionary using a table.
"""

from graphviz import Digraph

class TrackedDict(dict):
    """
    Tracks changes to a dictionary data structure and triggers creation of new visualization
    Args:
        dict: the dictionary data structure to track
    """

    def update(self, iterable):
        """
        Sets the value of a key-value pair and checks the keys of the dictionary
        Args:
            key (Any): key of the key-value pair to be set
            value (Any): value to be set for the specified key
        """
        super().update(iterable)
        keys = list(iterable.keys())
        Dict.create_viz(self, self, keys)


    def pop(self, key):
        """
        Removes a key-value pair given the key.
        Args:
            key (Any): key of the key-value pair to be removed
        Raises:
            KeyError: If the element to be removed is not in the dictionary.
        """
        super().pop(key)
        Dict.create_viz(self, self)


class Dict:
    """
    Create graphviz visualization for dictionary data structure
    """

    filenum = 1

    def see(self, func, data):
        """
        Creates a visualization for the initial dictionary and starts tracking
        a given dictionary as it changes throughout a given function.
        Args:
            func (function): function that the dictionary is being altered through
            data (dict): dictionary to track
        """
        Dict.create_viz(self, data)
        data = TrackedDict(data)
        if func is not None:
            func(data)


    def create_viz(self, data, keys=None):
        """
        Creates and renders a visualization of the dictionary using graphviz
        Args:
            data (dict): dictionary that is being visualized
            key (iterable): optional list of keys of new key-value pairs
        """

        if keys is None:
            keys = {}

        di_graph = Digraph('Dict', filename=f'dict{Dict.filenum}.gv')
        Dict.filenum += 1
        di_graph.attr(rankdir='LR')

        with di_graph.subgraph(name='cluster_Dict') as subgraph:
            subgraph.attr(label='Dictionary')
            subgraph.attr(style='filled')
            subgraph.attr(color='lightgrey')
            subgraph.node_attr.update(style='filled', color='white')

            # Create nodes for each key-value pair in the dictionary
            for k, val in data.items():
                if isinstance(val, dict):  # if value is a nested dictionary
                    subgraph.node(str(k),
                                  label=str(k),
                                  shape='rectangle',
                                  style='filled',
                                  color='lightblue2',)

                    for nested_k, nested_v in val.items():
                        if nested_k in keys:
                            subgraph.node(str(nested_k),
                                          label=f"{str(nested_k)}: {str(nested_v)}",
                                          style='filled',
                                          color='green',)

                        else:
                            subgraph.node(str(nested_k), label=f"{str(nested_k)}: {str(nested_v)}")

                        # Add an edge from parent node to child node
                        subgraph.edge(str(k), str(nested_k))

                else:  # if value is not a nested dictionary

                    if k in keys:
                        subgraph.node(str(k),
                                      label=f"{str(k)}: {str(val)}",
                                      style='filled',
                                      color='green',)
                    else:
                        subgraph.node(str(k), label=f"{str(k)}: {str(val)}")

        # Render the graph to a file
        di_graph.view()
