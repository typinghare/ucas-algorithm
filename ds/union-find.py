# author: ShotgunThinker

# A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into
# a number of disjoint (non-overlapping) subsets.
# A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
# 1. Find: Determine which subset a particular element is in. This can be used for determining if two elements
#    are in the same subset.
# 2. Union: Join two subsets into a single subset.
# see: https://www.geeksforgeeks.org/union-find/
# see: https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

class UnionFind:
    def __init__(self, n):
        """
        Initialize <parent>, each element is the only one in its subset, we can assume that it point to itself.
        So <parent> is shaped like [0, 1, 2, ..., n].
        We define the element that points to itself as "master node" of its subset. At the beginning, each element
        is a master node.
        <parent> can be seen as a dict which mapping is: node index => parent node index, it can also be represented
        as a forest
        Rank is the depth of a subset tree.
        :param n: the number of elements in graph.
        """
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i) -> int:
        """
        Find the master node of subset that contains i.
        :param i: an element to be found.
        :return: the master node of subset that contains i.
        """
        if self.parent[i] == i:
            # element i is master node, it'll be returned directly.
            return i
        else:
            # element i is not master node, we keep finding the element it points by recurse.
            # to compress the path, we relinked i to the master node of its subset.
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def union(self, i, j):
        """
        To union element i and j, two subsets that contain i or j is joined.
        :param i: the first element to be unionized
        :param j: the second element to be unionized
        """
        # all elements in subset that contains i are relinked to the master node of subset that contains j,
        # which realize the join of two subsets.
        self.parent[self.find(i)] = self.find(j)

    def unionByRank(self, i, j):
        """
        To union element i and j, two subsets that contain i or j is joined.
        :param i: the first element to be unionized
        :param j: the second element to be unionized
        """
        x, y = self.find(i), self.find(j)
        if self.rank[x] <= self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x

        # particularly, if their ranks are the same, add 1 on rank[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
