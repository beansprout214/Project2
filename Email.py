# Name: Chris Gallazeski
# Course: CMPSC 132
# File Name: Email.py
# Date: 12/12/24
#
# Description: Contains the Email class


class Email():
    def __init__(self,
                 address : str,
                 email_type : str,
                 ):
        self.__address = address
        self.__type = email_type

    def __str__(self):
        return (f"Address: {self.__address}\n"
                f"Type: {self.__type}")

    # Getters
    def get_address(self):
        return self.__address

    def get_type(self):
        return self.__type

    # Setters
    def set_address(self, address):
        self.__address = address

    def set_type(self, email_type):
        self.__type = email_type