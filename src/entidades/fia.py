from entidades.team import Team
from entidades.car import Car
from entidades.employee import Employee
from entidades.driver import Driver
from entidades.reserve_driver import ReserveDriver
from entidades.mechanic import Mechanic
from entidades.team_principal import TeamPrincipal
from entidades.race import Race
from utils import insert_nbr_list, insert_str_info, insert_number_info, select_employee_type


class Fia:
    def __init__(self):
        self.__team_employees: list[Employee] = []
        self.__teams: list[Team] = []
        self.__cars: list[Car] = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def add_team_employee(self):
        print("Agregar Empleado:")
        print("-----------------")
        ci = insert_number_info("Ingrese CI: ")
        #validar si empleado ya existe
        name = insert_str_info("Ingrese nombre: ")
        salary = insert_number_info("Ingrese salario: ")
        age = insert_number_info("Ingrese edad: ")
        country = insert_str_info("Ingrese pais: ")
        employee_type = select_employee_type()
        employee: Employee = None
        match employee_type:
            case 1:
                car_nbr = insert_number_info("Ingrese numero de auto: ")
                score = int(insert_number_info("Ingrese puntaje: "))
                if score > 99 or score < 0:
                    raise Exception("El puntaje debe ser entre 0 y 99")
                employee = Driver(ci, name, salary, age, country, car_nbr, score)
            case 2:
                car_nbr = insert_number_info("Ingrese numero de auto: ")
                score = insert_number_info("Ingrese puntaje: ")
                if score > 99 or score < 0:
                    raise Exception("El puntaje debe ser entre 0 y 99")
                employee = ReserveDriver(ci, name, salary, age, country, car_nbr, score)
            case 3:
                score = insert_number_info("Ingrese puntaje: ")
                if score > 99 or score < 0:
                    raise Exception("El puntaje debe ser entre 0 y 99")
                employee = Mechanic(ci, name, salary, age, country, score)
            case 4:
                employee = TeamPrincipal(ci, name, salary, age, country)
        self.__team_employees.append(employee)
        return True

    def add_car(self):
        model = insert_str_info("Ingrese modelo: ")
        year = insert_number_info("Ingrese año: ")
        score = insert_number_info("Ingrese puntaje: ")
        self.__cars.append(Car(model, year, score))

    def add_team(self):
        name = insert_str_info("Ingrese nombre: ")
        team = Team(name)
        car_model = insert_str_info("Ingrese modelo de auto: ")
        try:
            car_index = self.__cars.index(Car(car_model, 0 , 0))
        except ValueError: 
            raise Exception(f"El auto modelo {car_model} no existe")
        car = self.__cars[car_index]
        team.car = car
        while len(team.mechanics) != 8 or len(team.drivers) < 2 or team.team_principal == None or team.reserve_driver == None:
            ci = insert_number_info("Ingrese CI del empleado: ")
            employees = [ employee for employee in self.__team_employees if employee.ci == ci ]
            if len(employees) == 0:
                raise Exception("El empleado no existe")
            employee = employees[0]
            if isinstance(employee, TeamPrincipal):
                team.principal = employee
                print("El empleado es jefe de equipo")
            if isinstance(employee, Driver):
                if len(team.drivers) == 2:
                    print("El equipo ya tiene 2 pilotos titulares")
                else:
                    team.drivers.append(employee)
                    print("El empleado es un conductor")
            if isinstance(employee, ReserveDriver):
                team.reserve_driver = employee
                print("El empleado es un piloto de reserva")
            if isinstance(employee, Mechanic):
                team.mechanics.append(employee)
                print("El empleado es un mecanico")
        self.__teams.append(team)

    def simulate_race(self):
        drivers_out = insert_nbr_list("Ingrese todos los nro de autos que abandonan la carrera separados por coma: ")
        drivers_with_pit_errors = insert_nbr_list("Ingrese todos los nro de autos que tuvieron errores en los pits (separados por coma): ")
        drivers_penalized = insert_nbr_list("Ingrese todos los nro de autos que fueron penalizados (separados por coma): ")
        
        race = Race(self.__teams)
        self.__add_drivers_with_problems(race, drivers_out, drivers_with_pit_errors, drivers_penalized)
        results = race.simulate()
        print("Resultados de la carrera:")
        print("-------------------------")
        for pos, driver in enumerate(results):
            driver.add_points(pos+1)
            print(f"{pos+1}. {driver.name}")
        print("-------------------------")

    def top_10_drivers(self):
        drivers = [driver for team in self.__teams for driver in team.drivers] + [team.reserve_driver for team in self.__teams]
        drivers.sort(key=lambda driver: driver.points, reverse=True)
        print("Top 10 conductores:")
        print("-------------------------")
        for pos, driver in enumerate(drivers[:10]):
            print(f"{pos+1}. {driver.name}")
        print("-------------------------")

    def constructors_table(self):
        self.__teams.sort(key=lambda team: sum([driver.points for driver in team.drivers]) + team.reserve_driver.points, reverse=True)
        print("Campeonato de constructores:")
        print("-------------------------")
        for pos, team in enumerate(self.__teams):
            print(f"{pos+1}. {team.name}")
        print("-------------------------")

    def top_5_best_pay(self):
        drivers = [driver for team in self.__teams for driver in team.drivers] + [team.reserve_driver for team in self.__teams]
        drivers.sort(key=lambda driver: driver.salary, reverse=True)
        print("Top 5 conductores mejor pago:")
        print("-------------------------")
        for pos, driver in enumerate(drivers[:5]):
            print(f"{pos+1}. {driver.name}")
        print("-------------------------")

    def top_3_most_skilled(self):
        drivers = [driver for team in self.__teams for driver in team.drivers] + [team.reserve_driver for team in self.__teams]
        drivers.sort(key=lambda driver: driver.score, reverse=True)
        print("Top 3 pilotos con mayor habilidad:")
        print("-------------------------")
        for pos, driver in enumerate(drivers[:3]):
            print(f"{pos+1}. {driver.name}")
        print("-------------------------")
    
    def team_principals(self):
        principals = [[team.team_principal.name, team.name] for team in self.__teams]
        principals.sort(key=lambda x: x[0])
        print("Team Principals:")
        print("-------------------------")
        for principal in principals:
            print(f"{principal[0]} ({principal[1]})")
        print("-------------------------")
    
    def __add_drivers_with_problems(self, race, drivers_out, drivers_with_pit_errors, drivers_penalized):
        for driver_nbr in drivers_out:
            race.add_driver_out(driver_nbr)
        for driver_nbr in drivers_with_pit_errors:
            race.add_pit_error_driver(driver_nbr)
        for driver_nbr in drivers_penalized:
            race.add_penlized_driver(driver_nbr)
