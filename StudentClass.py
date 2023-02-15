from datetime import date


class Student:

    def __init__(self, StudentID, Name, dob, Classifications):
        self.__id = StudentID
        self.__name = Name
        self.__birth = dob
        self.__classification = Classifications
        self.__agenow = 0
        self.__registration = ""

    def age(self):
        today = date.today()
        year = today.year
        month = today.month

        datefixed = self.__birth.split('/')
        ageYear = datefixed[2]

        if month > int(datefixed[2]):
            self.__agenow = year - int(ageYear)
        else:
            self.__agenow = year - int(ageYear) - 1

    def register(self):
        if self.__classification == "F":
            self.__registration = "4/10 thru 4/12"
        elif self.__classification == "S":
            self.__registration = "4/7 thru 4/9"
        elif self.__classification == "Jr":
            self.__registration = "4/4 thru 4/6"
        elif self.__classification == "Sr":
            self.__registration = "4/1 thru 4/3"

    def get_age(self):
        return self.__agenow

    def get_registration(self):
        return self.__registration
