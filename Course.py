class Course():
    def __init__(self,
                 course_number,
                 semester_taken,
                 delivery_method,
                 status,
                 grade
                 ):
        self.__course_number = course_number
        self.__semester_taken = semester_taken
        self.__delivery_method = delivery_method
        self.__status = status
        self.__grade = grade

    # Getters
    def get_course_number(self):
        return self.__course_number

    def get_semester_taken(self):
        return self.__semester_taken

    def get_delivery_method(self):
        return self.__delivery_method

    def get_status(self):
        return self.__status

    def get_grade(self):
        return self.__grade

    # Setters
    def set_course_number(self, course_number):
        self.__course_number = course_number

    def set_semester_taken(self, semester_taken):
        self.__semester_taken = semester_taken

    def set_delivery_method(self, delivery_method):
        self.__delivery_method = delivery_method

    def set_status(self, status):
        self.__status = status

    def set_grade(self, grade):
        self.__grade = grade
