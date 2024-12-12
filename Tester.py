# Name: Hunter Becker
# Course: CMPSC 132
# File Name: Tester.py
# Date: 12/12/24
#
# Description: Contains testing information
# 3 Testing students
# 1 Testing advisor


from PhoneNumber import PhoneNumber
from Semester import Semester
from Address import Address
from Student import Student
from Email import Email
from Date import Date


from LinkedList import LinkedList
from Advisor import Advisor
from Course import Course
from Name import Name


michael_jordan_course_list = LinkedList()
michael_jordan_course_list.insert(
    Course("KIN101", Semester("Fall", 2023), "In-Person", "Passed", "B+")
)
michael_jordan_course_list.insert(
    Course("BBA202", Semester("Spring", 2024), "In-Person", "Passed", "B")
)
michael_jordan_course_list.insert(
    Course("HIST305", Semester("Fall", 2024), "Online", "Passed", "A-")
)
michael_jordan = Student(
    Name("Michael", "Jeffrey", "Jordan"),
    1011,
    Address(
        "456 Basketball Blvd", "Chicago", "Illinois", 60612, "Home"
    ),
    [Email("michael@nba.com", "Work")],
    [PhoneNumber(1234567893, "Mobile")],
    Date(2, 17, 1963),  # birth date, MM/DD/YY format
    Date(9, 1, 2023),  # acceptance date, MM/DD/YY format
    Semester("Fall", 2023),  # start semester
    "Kinesiology",  # intended major
    michael_jordan_course_list
)


tony_stark_course_list = LinkedList()
tony_stark_course_list.insert(
    Course("ENGR101", Semester("Fall", 2023), "In-Person", "Passed", "A")
)
tony_stark_course_list.insert(
    Course("PHYS201", Semester("Spring", 2024), "In-Person", "Passed", "A")
)
tony_stark_course_list.insert(
    Course("CS101", Semester("Fall", 2024), "Online", "Passed", "A-")
)
tony_stark = Student(
    Name("Tony", "Edward", "Stark"),
    456,
    Address(
        "10880 Malibu Point", "Malibu", "California", 90265, "Home"
    ),
    [Email("tony@starkindustries.com", "Work")],
    [PhoneNumber(1234567891, "Mobile")],
    Date(5, 29, 1970),  # birth date, MM/DD/YY format
    Date(9, 1, 2023),  # acceptance date, MM/DD/YY format
    Semester("Fall", 2023),  # start semester
    "Engineering",  # intended major
    tony_stark_course_list
)


frank_ocean_course_list = LinkedList()
frank_ocean_course_list.insert(
    Course("MUS101", Semester("Fall", 2023), "In-Person", "Passed", "A")
)
frank_ocean_course_list.insert(
    Course("LIT204", Semester("Spring", 2024), "In-Person", "Passed", "A")
)
frank_ocean_course_list.insert(
    Course("ART301", Semester("Fall", 2024), "In-Person", "Passed", "A-")
)
frank_ocean = Student(
    Name("Frank", "Christopher", "Ocean"),
    2024,
    Address(
        "123 Ocean Avenue", "Long Beach", "California", 90802, "Home"
    ),
    [Email("frank@music.com", "Personal")],
    [PhoneNumber(1234567894, "Mobile")],
    Date(10, 28, 1987),  # birth date, MM/DD/YY format
    Date(9, 1, 2023),  # acceptance date, MM/DD/YY format
    Semester("Fall", 2023),  # start semester
    "Music",  # intended major
    frank_ocean_course_list
)


kendrick_llamar_advisee_list = LinkedList()
kendrick_llamar_advisee_list.insert(frank_ocean)
kendrick_llamar_advisee_list.insert(michael_jordan)
kendrick_llamar_advisee_list.insert(tony_stark)
kendrick_llamar = Advisor(
    Name("Kendrick","","Llamar"),
    "Dr.",
    "Music",
    kendrick_llamar_advisee_list
)


students = [frank_ocean,michael_jordan,tony_stark]
advisors = [kendrick_llamar]