# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Semester.py
# Date: 12/12/24
#
# Description: Contains the Semester class


class Semester():
    def __init__(self,
                 season : str,
                 year : int,
                 ):
        self.__season = season
        self.__year = year

    def __str__(self):
        return f"Semester: {self.__season} {self.__year}"

    # Getters
    def get_season(self):
        return self.__season

    def get_year(self):
        return self.__year

    # Setters
    def set_season(self, season : str):
        self.__season = season

    def set_year(self, year : int):
        self.__year = year