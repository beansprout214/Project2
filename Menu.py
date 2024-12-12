# Name: Chris Gallazeski
# Course: CMPSC 132
# File Name: Menu.py
# Date: 11/08/24
#
# Description: Allows for the organization of the Student class in a single list


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Email import Email
from Date import Date
from Name import Name

from Student import Student
from Tester import students


# Utilities
# Allows for type and integrity checks to ensure input is as expected

def is_int(data):
    if (data is False) or (data is None):
        return False
    try:
        casted = int(data)
        return True
    except ValueError:
        return False

def input_integer():
    print(f"")
    user_input = ""
    while not is_int(user_input):
        user_input = input()
        if not is_int(user_input):
            print("Field only accepts integer values.")
    print(f"")
    return int(user_input)

def input_string():
    print(f"")
    user_input = 1
    while is_int(user_input) or user_input == "":
        user_input = input()
        if is_int(user_input):
            print("Field only accepts string values.")
        if user_input == "":
            print("Field does not accept empty strings.")
    print(f"")
    return user_input


# Functions for object creation
# Handles the creation of objects like Emails, Dates, etc.

def create_new_phone_number_list():
    print(f"Creating a new phone number list!")
    phone_number_list = [create_new_phone_number()]
    while True:
        print(f"Would you like to add more phone numbers?\n"
              f"1 - Yes      2 - No\n")
        user_input = input_integer()
        if user_input != 1:
            break

        new_phone_number = create_new_phone_number()

        print(f"Are you sure you'd lke to add\n"
              f"the following phone number?\n"
              f"{new_phone_number}\n"
              f"1 - Yes      2 - No")

        cancel = input_integer() != 1
        if cancel:
            print(f"Phone number successfully discarded.")
            continue

        print(f"Phone number successfully added.")
        phone_number_list.append(new_phone_number)
    return phone_number_list

def create_new_phone_number():
    print(f"Creating a new phone number!")
    print(f"Enter the number:")
    new_phone_number = input_integer()
    print(f"Enter the number type (ex. Home, Mobile):")
    new_phone_number_type = input_string()
    return PhoneNumber(new_phone_number,new_phone_number_type)

def create_new_semester():
    print(f"Creating a new semester!")
    
    print(f"Please enter the semester season. (ex. Fall, Spring)")
    new_season = input_string()
    print(f"Please enter the year. (ex. 1994, 2013)")
    new_year = input_integer()

    new_semester = Semester(
        new_season,
        new_year
        )
    return new_semester 

def create_new_address():
    print(f"Creating a new address!")

    print(f"Please enter the street name.")
    new_street = input_string()
    print(f"Please enter the city name.")
    new_city = input_string()
    print(f"Please enter the state name.")
    new_state = input_string()
    print(f"Please enter the zip code.")
    new_zip = input_integer()
    print(f"Please enter the address type. (ex. Business, Home)")
    new_type = input_string()
    
    new_address = Address(
        new_street,
        new_city,
        new_state,
        new_zip,
        new_type
    )
    return new_address

def create_new_email_list():
    print(f"Creating a new email list!")
    email_list = [create_new_email()]
    while True:
        print(f"Would you like to add more emails?\n"
              f"1 - Yes      2 - No")
        user_input = input_integer()
        if user_input != 1:
            break

        new_email = create_new_email()

        print(f"Are you sure you'd lke to add\n"
              f"the following email?\n"
              f"{new_email}\n"
              f"1 - Yes      2 - No")

        cancel = input_integer() != 1
        if cancel:
            print(f"Email successfully discarded.")
            continue

        print(f"Email successfully added.")
        email_list.append(new_email)
    return email_list

def create_new_email():
    print(f"Creating a new email!")
    print(f"Please enter the email address.")
    new_address = input_string()
    print(f"Please enter the email type. (ex. Personal, School)")
    new_type = input_string()
    return Email(new_address,new_type)

def create_new_date():
    print(f"Creating a new date!")

    print(f"Please enter the month:")
    new_month = input_integer()
    print(f"Please enter the day:")
    new_day = input_integer()
    print(f"Please enter the year:")
    new_year = input_integer()

    new_date = Date(
        new_month,
        new_day,
        new_year
    )
    return new_date

def create_new_name():
    print(f"Creating a new name!")
    print(f"Please enter the first name:")
    first_name = input_string()
    print(f"Please enter the last name:")
    last_name  = input_string()

    middle_name = ""
    print(f"Would you like to add\n"
          f"a middle name?\n"
          f"1 - Yes      2 - No")
    cancel = input_integer() != 1
    if not cancel:
        print(f"Please enter the middle name:")
        middle_name = input_string()
    return Name(first_name, middle_name, last_name)

def create_new_student():
    print(f"Creating a new student!")

    print(f"Please enter their name:")
    new_name = input_string()
    print(f"Please enter their student ID")
    new_id = input_integer()
    print(f"Please enter their mailing address:")
    new_mailing_address = create_new_address()
    print(f"Please enter their email address:")
    new_email_address_list = create_new_email_list()
    print(f"Please enter a list of their phone numbers:")
    new_phone_number_list = create_new_phone_number_list()
    print(f"Please enter their birth date:")
    new_birth_date = create_new_date()
    print(f"Please enter their acceptance date:")
    new_acceptance_date = create_new_date()
    print(f"Please enter their start semester:")
    new_start_semester = create_new_semester()
    print(f"Please enter their intended major:")
    new_intended_major = input_string()

    new_student = Student(
        new_name,
        new_id,
        new_mailing_address,
        new_email_address_list,
        new_phone_number_list,
        new_birth_date,
        new_acceptance_date,
        new_start_semester,
        new_intended_major
    )
    print(f"{new_student}\n\n"
          f"Are you sure you'd like to create this student?\n"
          f"1 - Yes      2 - No")

    cancel = input_integer() != 1

    if cancel:
        print(f"Student creation cancelled.")
        return False
    return new_student


# Functions for student management
# Handles the manipulation of Student objects within the Students list

def pick_student():
    if len(students) == 0:
        print(f"Cannot proceed further; No students in list!")
        return False

    index = 1

    print(f"Pick a student from this list, or 0 to cancel:")
    for student in students:
        print(f"{index} : {student.get_name()}")
        index += 1

    user_choice = input_integer()

    while (user_choice < 0) or (user_choice > len(students)):
        print(f"Selection outside of range!")
        user_choice = input_integer()

    if user_choice == 0:
        print(f"No student selected.")
        return False,None

    index = user_choice - 1

    return students[index],index

def edit_student():
    print(f"What attribute would you like to edit?\n"
          f"")

    user_choice = input_integer()

    if user_choice == 1:
        new_name = input_string()
        student.set_name(new_name)

    elif user_choice == 2:
        new_id = input_integer()
        student.set_id(new_id)

    elif user_choice == 3:
        new_mailing_address = create_new_address()
        student.set_mailing_address(new_mailing_address)

    elif user_choice == 4:
        new_email_address = create_new_email()
        student.set_email_address(new_email_address)

    elif user_choice == 5:
        new_phone_number_list = create_new_phone_number_instance()
        student.set_phone_number(new_phone_number_list)

    elif user_choice == 6:
        new_birth_date = create_new_date()
        student.set_birth_date(new_birth_date)

    elif user_choice == 7:
        new_acceptance_date = create_new_date()
        student.set_acceptance_date(new_acceptance_date)

    elif user_choice == 8:
        new_start_semester = create_new_semester()
        student.set_start_semester(new_start_semester)

    elif user_choice == 9:
        new_intended_major = input_string()
        student.set_intended_major(new_intended_major)

    else:
        print(f"Nothing selected! Cancelling edit.")
    
    return

def add_student():
    new_student = create_new_student()
    if new_student:
        students.append(new_student)
        return True
    return False

def delete_student():
    print(f"Choose a student to delete:")
    student,index = pick_student()

    cancel = True

    if student:
        print(f"{student}\n"
              f"Are you sure you'd like\n"
              f"to delete this student?\n"
              f"1 - Yes      2 - No")
        cancel = input_integer() != 1

    if cancel:
        print(f"Student deletion cancelled.")
        return False

    students.pop(index)
    print(f"Student deleted successfully.")
    return True

def display_student():
    print(f"Choose a student to display:")
    student,index = pick_student()
    if student:
        print(f"{student}\n\n")
        return
    print(f"Student display cancelled.")
    return



# Menu definition
# Handles user input and uses the other defined functions accordingly

def menu():
    print(f"Welcome to the student and advisor management program!")
    user_option = 0
    while user_option != 5:
        print(f"What would you like to do?\n"
              f"1 - Add a student to the list\n"
              f"2 - Edit a student from the list\n"
              f"3 - Delete a student from the list\n"
              f"4 - Display a student's info\n"
              f"5 - Exit the application")

        user_option = input_integer()

        if user_option == 1:
            add_student()
        elif user_option == 2:
            edit_student()
        elif user_option == 3:
            delete_student()
        elif user_option == 4:
            display_student()

    print(f"Thank you for using this student and advisor management program.")


# Main

if __name__ == '__main__':
    menu()