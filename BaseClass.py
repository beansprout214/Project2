# Name: Hunter Becker
# Course: CMPSC 132
# File Name: BaseClass.py
# Date: 11/08/24
#
# Description: Contains the BaseClass class
# Exists to allow other classes to inherit the universal display method


class BaseClass():
    def display(self):
        def display_recursive(object, header):
            if isinstance(object, int) or isinstance(object, str):
                print(f"{header} : {object}")
                return
            elif isinstance(object, list):
                for curr in object:
                    display_recursive(curr, header)
                    return

            class_name = object.__class__.__name__
            header = len(header) > 0 and f"{header} : {class_name}" or f"{class_name}"
            for attr, value in object.__dict__.items():
                display_recursive(value, header)

        print(f"{self.__class__.__name__} Class")

        attribute_truncate_index = len(self.__class__.__name__) + 1
        for attr, value in self.__dict__.items():
            display_recursive(value, f"{attr[attribute_truncate_index:]}")