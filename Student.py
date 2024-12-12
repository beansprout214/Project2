# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Address.py
# Date: 11/08/24
#
# Description: Contains the Student class
# Attributes: name, id, mailing_address, email_address, phone_number, birth_date, acceptance_date, start_semester, intended_major


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date
from Name import Name

from LinkedList import LinkedList
from Node import Node


class Student():
    def __init__(self,
                 name : str,
                 id : int,
                 mailing_address : Address,
                 email_address : [],
                 phone_number : [],
                 birth_date : Date,
                 acceptance_date : Date,
                 start_semester : Semester,
                 intended_major : str,
                 course_list : LinkedList
                 ):
        self.__name = name
        self.__id = id
        self.__mailing_address = mailing_address
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__birth_date = birth_date
        self.__acceptance_date = acceptance_date
        self.__start_semester = start_semester
        self.__intended_major = intended_major
        self.__course_list = course_list

    def __str__(self):
        str_email = ""
        index = 0
        for email in self.__email_address:
            str_email += (f"Email {index + 1} Type: {email.get_type()}\n"
                          f"Email {index + 1} Address: {email.get_address()}\n")
            index += 1

        str_phone_number = ""
        index = 0
        for phone_number in self.__phone_number:
            str_phone_number += (f"Phone Number {index + 1} Type: {phone_number.get_type()}\n"
                                 f"Phone Number {index + 1} Number: {phone_number.get_number()}\n")
            index += 1

        str_course_list = ""
        index = 0
        course_list = self.__course_list
        if course_list and not course_list.get_head() is None:
            curr_node = course_list.get_head()
            while not curr_node is None:
                course = curr_node.get_data()
                str_course_list += (f"Course {index + 1} Number: {course.get_course_number()}\n"
                                    f"Course {index + 1} Semester Taken: {course.get_semester_taken()}\n"
                                    f"Course {index + 1} Delivery Method: {course.get_delivery_method()}\n"
                                    f"Course {index + 1} Status: {course.get_status()}\n"
                                    f"Course {index + 1} Grade: {course.get_grade()}\n")
                curr_node = curr_node.get_next()
                index += 1

        return (f'Name: {self.__name}\n'
                f'ID: {self.__id}\n'
                f'Mailing Address: {self.__mailing_address}\n'
                f'{str_email}'
                f'{str_phone_number}'
                f'Birth Date: {self.__birth_date}\n'
                f'Acceptance Date: {self.__acceptance_date}\n'
                f'Starting Semester: {self.__start_semester}\n'
                f'Intended Major: {self.__intended_major}\n'
                f'{str_course_list}')

    # Getters
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_mailing_address(self):
        return self.__mailing_address

    def get_email_address(self):
        return self.__email_address

    def get_phone_number(self):
        return self.__phone_number

    def get_birth_date(self):
        return self.__birth_date

    def get_acceptance_date(self):
        return self.__acceptance_date

    def get_start_semester(self):
        return self.__start_semester

    def get_intended_major(self):
        return self.__intended_major

    def get_course_list(self):
        return self.__course_list

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_id(self, id: int):
        self.__id = id

    def set_mailing_address(self, mailing_address: Address):
        self.__mailing_address = mailing_address

    def set_email_address(self, email_address: Email):
        self.__email_address = email_address

    def set_phone_number(self, phone_number: PhoneNumber):
        self.__phone_number = phone_number

    def set_birth_date(self, birth_date: Date):
        self.__birth_date = birth_date

    def set_acceptance_date(self, acceptance_date: Date):
        self.__acceptance_date = acceptance_date

    def set_start_semester(self, start_semester: Semester):
        self.__start_semester = start_semester

    def set_intended_major(self, intended_major: str):
        self.__intended_major = intended_major

    def set_course_list(self, course_list: LinkedList):
        self.__course_list = course_list