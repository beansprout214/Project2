class Advisor():
    def __init__(self,
                 name,
                 title,
                 department,
                 advisee_list
                 ):
        self.__name = name
        self.__title = title
        self.__department = department
        self.__advisee_list = advisee_list

    def __str__(self):
        str_advisee_list = ""
        index = 0
        advisee_list = self.__advisee_list
        if advisee_list and not advisee_list.get_head() is None:
            curr_node = advisee_list.get_head()
            while not curr_node is None:
                advisee = curr_node.get_data()
                str_advisee_list += f"Advisee {index + 1}: {advisee.get_name()}"
                curr_node = curr_node.get_next()
                index += 1

        return (f'Name: {self.__name}\n'
                f'Title: {self.__title}\n'
                f'Department: {self.__department}\n'
                f'{str_advisee_list}')

    # Getters
    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def get_department(self):
        return self.__department

    def get_advisee_list(self):
        return self.__advisee_list

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_title(self, title):
        self.__title = title

    def set_department(self, department):
        self.__department = department

    def set_advisee_list(self, advisee_list):
        self.__advisee_list = advisee_list
