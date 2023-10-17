from entidades.employee import Employee
from entidades.driver import Driver
from entidades.mechanic import Mechanic
from entidades.team_principal import TeamPrincipal
from entidades.team import Team
from entidades.car import Car
from utils import insert_str_info, insert_number_info, select_employee_type


class Fia:
    def __init__(self):
        self.__team_employees: list[Employee] = []
        self.__teams = list[Team] = []
        self.__cars = list[Car] = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def add_team_employee(self):
        print("Agregar Empleado:")
        print("-----------------")
        ci = insert_number_info("Ingrese CI: ")
        name = insert_str_info("Ingrese nombre: ")
        salary = insert_number_info("Ingrese salario: ")
        age = insert_number_info("Ingrese edad: ")
        country = insert_str_info("Ingrese pais: ")
        employee_type = select_employee_type()
        employee: Employee = None
        match employee_type:
            case "1":
                car_nbr = insert_number_info("Ingrese numero de auto: ")
                score = insert_number_info("Ingrese puntaje: ")
                employee = Driver(ci, name, salary, age, country, car_nbr, score)
            case "2":
                score = insert_number_info("Ingrese puntaje: ")
                employee = Mechanic(ci, name, salary, age, country, score)
            case "3":
                employee = TeamPrincipal(ci, name, salary, age, country)
        self.__team_employees.append(employee)
        return True

    def add_team(self):
        pass
    
    def add_car(self):
        pass
