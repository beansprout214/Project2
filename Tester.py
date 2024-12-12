# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Address.py
# Date: 11/08/24
#
# Description: Tests the student and aggregate class


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Student import Student
from Email import Email
from Date import Date
from Name import Name


from LinkedList import LinkedList
from Node import Node


student1_phone_number = PhoneNumber(
    9876543210,
    "Personal"
)

student1_semester = Semester(
    "Spring",
    2025
)

student1_address = Address(
    "Baker Street",
    "Gotham",
    "New York",
    67890,
    "Temporary"
)

student1_email = Email(
    "another_example@mail.com",
    "Work"
)
student1_email2 = Email(
    "hello@hi.com",
    "Personal"
)

student1_birth_date = Date(
    12,
    25,
    1995
)

student1_acceptance_date = Date(
    8,
    15,
    2024
)

student1_student = Student(
    Name("Jane","","Doe"), # Student Name
    456, # Student ID
    student1_address, # Student Mailing Address
    [student1_email,student1_email2], # Student Email Addresses (Contains at least 1 email address)
    [student1_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student1_birth_date, # Birth Date
    student1_acceptance_date, # Acceptance Date
    student1_semester, # Start semester
    "Engineering", # Student Intended Major
    None
)
student2_phone_number = PhoneNumber(
    1230984567,
    "Personal"
)

student2_semester = Semester(
    "Summer",
    2024
)

student2_address = Address(
    "155 Cornelia Street",
    "New York",
    "New York",
    10014,
    "Temporary"
)

student2_email = Email(
    "taylor.swift@music.com",
    "Personal"
)

student2_birth_date = Date(
    12,
    13,
    1989
)

student2_acceptance_date = Date(
    9,
    10,
    2024
)

student2_student = Student(
    Name("Taylor","","Swift"), # Student Name
    666, # Student ID
    student2_address, # Student Mailing Address
    [student2_email], # Student Email Addresses (Contains at least 1 email address)
    [student2_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student2_birth_date, # Birth Date
    student2_acceptance_date, # Acceptance Date
    student2_semester, # Start semester
    "Music", # Student Intended Major
    None
)

student3_phone_number = PhoneNumber(
    1234567890,
    "Work"
)

student3_semester = Semester(
    "Winter",
    2024
)

student3_address = Address(
    "10880 Malibu Point",
    "Malibu",
    "California",
    90265,
    "Permanent"
)

student3_email = Email(
    "tony.stark@starkindustries.com",
    "Work"
)

student3_birth_date = Date(
    5,
    29,
    1970
)

student3_acceptance_date = Date(
    9,
    1,
    2024
)

student3_student = Student(
    Name("Tony","","Stark"), # Student Name
    999, # Student ID
    student3_address, # Student Mailing Address
    [student3_email], # Student Email Addresses (Contains at least 1 email address)
    [student3_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student3_birth_date, # Birth Date
    student3_acceptance_date, # Acceptance Date
    student3_semester, # Start semester
    "Engineering", # Student Intended Major
    None
)
student4_phone_number = PhoneNumber(
    9876543210,
    "Home"
)

student4_semester = Semester(
    "Fall",
    2024
)

student4_address = Address(
    "4 Privet Drive",
    "Little Whinging",
    "Surrey",
    12345,
    "Temporary"
)

student4_email = Email(
    "hermione.granger@hogwarts.com",
    "School"
)

student4_birth_date = Date(
    9,
    19,
    1979
)

student4_acceptance_date = Date(
    8,
    10,
    2024
)

student4_student = Student(
    Name("Hermione","","Granger"), # Student Name
    888, # Student ID
    student4_address, # Student Mailing Address
    [student4_email], # Student Email Addresses (Contains at least 1 email address)
    [student4_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student4_birth_date, # Birth Date
    student4_acceptance_date, # Acceptance Date
    student4_semester, # Start semester
    "Magic", # Student Intended Major
    None
)
student5_phone_number = PhoneNumber(
    5551234567,
    "Personal"
)

student5_semester = Semester(
    "Spring",
    2025
)

student5_address = Address(
    "1007 Mountain Drive",
    "Gotham",
    "New Jersey",
    67890,
    "Permanent"
)

student5_email = Email(
    "bruce.wayne@wayneenterprises.com",
    "Work"
)

student5_birth_date = Date(
    2,
    19,
    1972
)

student5_acceptance_date = Date(
    9,
    15,
    2024
)

student5_student = Student(
    Name("Bruce","","Wayne"), # Student Name
    777, # Student ID
    student5_address, # Student Mailing Address
    [student5_email], # Student Email Addresses (Contains at least 1 email address)
    [student5_phone_number], # Student Phone Numbers (Contains at least 1 phone number)
    student5_birth_date, # Birth Date
    student5_acceptance_date, # Acceptance Date
    student5_semester, # Start semester
    "Business Administration", # Student Intended Major
    None
)


students = [student1_student, student2_student, student3_student, student4_student, student5_student]