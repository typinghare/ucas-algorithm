import numpy


class AdjacencyMatrixGraph:
    def __init__(self, vertex_number: int):
        # adjacent matrix
        self.am = numpy.zeros((vertex_number, vertex_number), int)

    def add_edge(self, tail, head):
        """
        Add an edge in-between <tail> and <head>
        """
        self.am[tail][head] = 1

    def remove_edge(self, tail, head):
        """
        Add an edge in-between <tail> and <head>
        """
        self.am[tail][head] = 0

