# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Node.py
# Date: 11/19/24
#
# Description: Contains the Node class
# Is a single node with data and pointer to the next node


class Node():
    def __init__(self,
                 data = None,
                 next = None):
        self.__data = data
        self.__next = next

    def get_next(self):
        return self.__next

    def get_data(self):
        return self.__data

    def set_next(self,
                 next):
        self.__next = next

    def set_data(self,
                 data):
        self.__data = data