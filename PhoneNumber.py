# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Address.py
# Date: 11/08/24
#
# Description: Contains the PhoneNumber class
# Attributes: number, type


class PhoneNumber():
    def __init__(self,
                 number : int,
                 type : str,
                 ):
        self.__number = number
        self.__type = type

    def __str__(self):
        return (f"Number: {self.__number}\n"
                f"Type: {self.__type}")

    # Getters
    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    # Setters
    def set_number(self, number: int):
        self.__number = number

    def set_type(self, type: str):
        self.__type = type