from abc import ABC

class Employee(ABC):

    def __init__(self, ci, name, salary, age, country):
        self.__ci = ci
        self.__name = name
        self.__salary = salary
        self.__age = age
        self.__country = country
    
    @property
    def ci(self):
        return self.__ci
    @ci.setter
    def ci(self, ci):
        self.__ci = ci
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
   
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country):
        self.__country = country
