class Node:
    def __init__(self, data=None):
        self.data = data  # data value
        self.next = None  # next node


class LinkedList:
    def __init__(self):
        self.first = None  # first node

    def size(self):
        """
        :return: the size of linked list.
        """
        size = 0
        node = self.first
        while node is not None:
            size += 1
            node = node.next
        return size

    def insert(self, index, data):
        """
        Insert a node at specified index.
        :param index: index at which the specified data is to be inserted.
        :param data: data to be inserted.
        """
        size = self.size()

        # raise error if index is greater than size
        if index > size:
            raise IndexError("Index out of range: " + index)

        # create a node which carries the data given
        node = Node(data)

        # if size equals to zero, the node will be the first node
        if size == 0:
            self.first = node
            return

        # if index equals to zero, the situation will be special
        if index == 0:
            node.next = self.first
            self.first = node
            return

        # link after last node if index equals to size
        if index == size:
            # get the last node
            last = self.node(index - 1)
            last.next = node
            return

        # common situation
        before = self.node(index - 1)
        node.next = before.next
        before.next = node

    def insertLast(self, data):
        """
        Append a node.
        """
        # get the last node
        last = self.node(self.size() - 1)
        last.next = Node(data)

    def node(self, index):
        """
        :param index: index of the specified node.
        :return: node at specified index.
        """
        node = self.first
        for i in range(index):
            node = node.next
        return node

    def check_index(self, index):
        """
        :param index: index of the specified node.
        :return: whether or not the index is legal.
        """
        size = self.size()
        if index < 0 or index >= size:
            raise IndexError('Index: ' + str(index) + ", Size: " + str(size))

    def get(self, index):
        """
        :param index: index of the specified node.
        :return: the data value of node at specified index.
        """
        self.check_index(index)
        return self.node(index).data

    def contains(self, data):
        """
        Whether or not list contains a node which data is equals to data given.
        :param data: specified data given
        """
        curr = self.first
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def set(self, index, new_data):
        """
        Update value of specified node.
        :param index: index of the node to update.
        :param new_data: data to be stored at the specified position.
        :return:
        """
        self.check_index(index)
        node = self.node(index)
        node.data = new_data

    def remove(self, index):
        """
        :param index: index of the node to remove.
        """
        self.check_index(index)

        # remove first node
        if index == 0:
            self.first = self.first.next
            return

        # remove last node
        size = self.size()
        if index == size - 1:
            node = self.node(index - 1)
            node.next = None
            return

        # common situation
        node = self.node(index - 1)
        node.next = node.next.next

    def print(self):
        """
        To print the linked list.
        """
        size = self.size()
        buffer = '[ '
        if size == 0:
            buffer += 'empty'
        else:
            curr = self.first
            buffer += str(curr.data)
            for i in range(size - 1):
                curr = curr.next
                buffer += ' -> ' + str(curr.data)

        print(buffer + ' ]')


class AdjacencyListGraph:
    def __init__(self, vertex_number: int):
        # vertex list
        self.vl: list = [LinkedList() for i in range(vertex_number)]

    def add_edge(self, tail, head):
        edge_list = self.vl[tail]
        if not edge_list.contains(head):
            self.vl[tail].insertLast(head)

    def remove_edge(self, tail, head):
        edge_list = self.vl[tail]
        curr = edge_list.first

        i, pos = 0, -1
        while curr is not None:
            if curr.data == head:
                pos = i
                break
            i += 1
            curr = curr.next
        if pos >= 0:
            edge_list.remove(pos)