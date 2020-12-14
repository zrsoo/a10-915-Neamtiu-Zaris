"""
Entities package
"""

# Imports
import itertools
import pickle

#


class Person:
    """
        The person class
    """

    # id - unique
    identification = itertools.count(1)

    #

    def __init__(self, name, phone_number):
        self.__name = name
        self.__phone_number = phone_number
        self.__id = next(self.identification)

    # Getters, setters

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self, name):
        self.__name = name

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @id.setter
    def id(self, id):
        self.__id = id

    # To str overload

    def __str__(self) -> str:
        return str(self.__id) + ".) " + self.name + "; " + self.phone_number


# Reading from text file

def read_persons_from_file(data_file):
    result = []
    try:
        file = open(data_file, "r")
        line = file.readline().strip()

        while len(line) > 0:
            line = line.split(';')
            result.append(Person(line[0], line[1]))
            line = file.readline().strip()

        file.close()
    except Exception as ex:
        print(ex)  # log the error
        raise ex

    return result


class Activity:
    """
        The activity class
    """

    # id - unique
    identification = itertools.count(1)

    #

    # List of person id's (contains the list of persons that perform the activity)
    # __li_persons = []

    def __init__(self, person_id, date, time, description):
        # self.__li_persons = []
        self.__id = next(self.identification)

        self.__li_persons = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    # Getters, setters

    @property
    def id(self):
        return self.__id

    @property
    def person_id_list(self):
        return self.__li_persons

    @property
    def date(self):
        return self.__date

    @property
    def time(self):
        return self.__time

    @property
    def description(self):
        return self.__description

    @date.setter
    def date(self, date):
        self.__date = date

    @time.setter
    def time(self, time):
        self.__time = time

    @description.setter
    def description(self, description):
        self.__description = description

    @id.setter
    def id(self, id):
        self.__id = id

    # To str overload

    def __str__(self) -> str:
        return str(self.__id) + ".) " + "Personal Id's: " + str(self.person_id_list) + "; " \
               + self.date + "; " + self.time + "; " + self.description


# Reading activities from file

def read_activities_from_file(data_file):
    result = []
    try:
        file = open(data_file, "r")
        line = file.readline().strip()

        while len(line) > 0:
            line = line.split(';')
            result.append(Activity(format_id_list(line[0]), line[1], line[2], line[3]))
            line = file.readline().strip()

        file.close()
    except Exception as ex:
        print(ex)  # log the error
        raise ex
    return result


def format_id_list(string):
    """
    Receives a string containing the list of id's of persons performing an activity
    :return: A list containing the id's
    """
    string = string[1:-1]
    li_ids = []
    for word in string.split(","):
        li_ids.append(int(word))
    # print(li_ids)
    return li_ids


# Reading from binary file


def read_binary_file(data_file):
    try:
        f = open(data_file, "rb")
        return pickle.load(f)
    except EOFError:  # If input file is empty
        return []
    except IOError as e:
        print(e)
        raise e