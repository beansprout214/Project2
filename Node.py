# Name: Chris Gallazeski
# Course: CMPSC 132
# File Name: Node.py
# Date: 12/12/24
#
# Description: Contains the Node class


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