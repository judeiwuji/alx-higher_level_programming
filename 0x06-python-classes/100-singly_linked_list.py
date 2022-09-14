#!/usr/bin/python3


"""This module defines a Node class."""


class Node:
    """A node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Instantiate a node for a linked list
        Args:
            data: (int)
            next_node: (int)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data value"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node"""
        if (value is None) or (type(value) is Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """This defines a singly linked list"""

    def __init__(self):
        """Instantiate a SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """Returns this list as string"""
        node = self.__head
        list_str = ""
        while node is not None:
            list_str += str(node.data)
            node = node.next_node
            if node is not None:
                list_str += "\n"
        return list_str

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)"""
        new_node = Node(value, None)

        if self.__head is not None:
            node = self.__head
            prev = None
            found = None
            while node is not None:
                if node.data > value:
                    found = node
                    break
                prev = node
                node = node.next_node

            if found is not None:
                new_node.next_node = found
                if prev is not None:
                    prev.next_node = new_node
                if found is self.__head:
                    self.__head = new_node
            else:
                prev.next_node = new_node
        else:
            self.__head = new_node
