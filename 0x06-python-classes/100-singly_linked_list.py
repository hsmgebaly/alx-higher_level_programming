#!/usr/bin/python3


"""Create a classes for the singly-linked list."""


class Node:
    """In a singly-linked list, represent a node."""

    def __init__(self, data, next_node=None):
        """Set-up a new node.

        The arguments will be as following:
            data (int): The new node's data.
            next_node (Node): The new Node's following node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The node's data can be retrieved or changed."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The Node's next_node can be retrieved or modified."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create a singly-linked list."""

    def __init__(self):
        """Set-up a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Create a new Node and add it to the singly linked list.

        The node is added to the list at the appropriate,
		numerically ordered position.

        The arguments will be as following:
            value (Node): Adding a new node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define a SinglyLinkedList's print() representation."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
