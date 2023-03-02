import os
from graphviz import Digraph

file_num = 1

class List:
    def __init__(self):
        file_num = 1

    def visualize(self, func, data):
        List.createViz(data, None)
        data = TrackedArray(data)
        func(data)

    def createViz(data, index):
        # TODO: add index labels

        global file_num

        g = Digraph('List', filename=f'see{file_num}_.gv')
        file_num = file_num + 1
        g.attr(rankdir='LR')
        
        # Create nodes for each element in the list
        for i, val in enumerate(data):
            node_style = 'filled' if i == index else ''
            node_fillcolor = 'green' if i == index else ''
            g.node(str(i), label=str(val), style=node_style, fillcolor=node_fillcolor)
        
        # Create edges between adjacent nodes
        edge_idx = (index - 1) if index is not None else -1
        for i in range(len(data) - 1):
            g.edge(str(i), str(i + 1))
        
        # Render the graph to a file
        g.view()
