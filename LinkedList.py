# Name: Hunter Becker
# Course: CMPSC 132
# File Name: LinkedList.py
# Date: 11/19/24
#
# Description: Contains the LinkedList class
# Is a singly linked list with a head and tail


class LinkedList():
    def __init__(self,
                 head = None,
                 tail = None):
        self.__head = None
        self.__tail = None
        if head:
            self.set_head(head)
        if tail:
            self.set_tail(tail)
        if (head or tail) and not (head and tail):
            node = tail or head
            self.set_head(node)
            self.set_tail(node)


    def get_head(self):
        return self.__head or None

    def get_tail(self):
        return self.__tail or None

    def set_head(self,
                 node):
        self.__head = node

    def set_tail(self,
                 node):
        self.__tail = node

    def append(self,
                 node):

        curr_tail = self.get_tail()

        if curr_tail:
            curr_tail.set_next(node)
            self.set_tail(node)
        else:
            self.set_head(node)
            self.set_tail(node)

    def prepend(self,
               node):

        curr_head = self.get_head()

        if curr_head:
            node.set_next(curr_head)
            self.set_head(node)
        else:
            self.set_head(node)
            self.set_tail(node)