# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Address.py
# Date: 12/12/24
#
# Description: Contains the Address class


class Address():
    def __init__(self,
                 street : str,
                 city : str,
                 state : str,
                 zip : int,
                 type : str,
                 ):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__type = type

    def __str__(self):
        return (f"Street: {self.__street}\n"
                f"City, State, Zip: {self.__city}, {self.__state} {self.__zip}\n"
                f"Type: {self.__type}")

    # Getters
    def get_street(self):
        return self.__street

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_type(self):
        return self.__type

    # Setters
    def set_street(self, street: str):
        self.__street = street

    def set_city(self, city: str):
        self.__city = city

    def set_state(self, state: str):
        self.__state = state

    def set_zip(self, zip: int):
        self.__zip = zip

    def set_type(self, type: str):
        self.__type = type