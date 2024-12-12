# Name: Chris Gallazeski
# Course: CMPSC 132
# File Name: LinkedList.py
# Date: 12/12/24
#
# Description: Contains the LinkedList class
# __len__ returns the length of the linked list
# __str__ returns the linked list's contents as a string
# insert(data) appends a new node with Data
# find(key) returns the node with data matching key, if it exists
# delete(key) deletes the node with data matching key, if it exists


from Node import Node


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


    def __len__(self):
        curr = self.__head
        if not curr:
            return 0
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count


    def __str__(self):
        str = ""
        curr = self.__head
        if curr is None:
            return "Empty"
        while curr:
            str += f"{curr.get_data()}"
            curr = curr.get_next()
        return str


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

    def insert(self,
               data):
        new_node = Node(data)
        curr_tail = self.__tail
        if curr_tail:
            curr_tail.set_next(new_node)
            self.__tail = new_node
            return
        self.__head = new_node
        self.__tail = new_node

    def find(self,
             key):
        curr = self.__head
        while curr and curr.get_data() != key:
            curr = curr.get_next()
        return curr

    def delete(self,
               key):
        node = self.find(key)
        if node is None:
            return

        if node == self.__head:
            self.__head = node.get_next()
            return

        prev = self.__head
        while prev.get_next() != node:
            prev = prev.get_next()
        prev.set_next(node.get_next())
        return