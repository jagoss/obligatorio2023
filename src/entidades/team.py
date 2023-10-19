from entidades import (Car, Driver, TeamPrincipal, Mechanic)

class Team:
    def __init__(self, name) -> None:
        self.__name = name
        self.__drivers : list[Driver]  = []
        self.__reserve_driver: Driver  = None
        self.__team_principal: TeamPrincipal = None
        self.__mechanics: list[Mechanic] = []
        self.__car: Car = None

    @property
    def name(self):
        return self.__name
    
    @name.setter   
    def name(self, name):
        self.__name = name

    @property
    def drivers(self):
        return self.__drivers
    
    @drivers.setter
    def drivers(self, drivers):
        self.__drivers = drivers

    @property
    def reserve_driver(self):
        return self.__reserve_driver
    
    @reserve_driver.setter
    def drivers(self, reserve_driver):
        self.__reserve_driver = reserve_driver

    @property
    def team_principal(self):
        return self.__team_principal
    @team_principal.setter
    def team_principal(self, team_principal):
        self.__team_principal = team_principal

    @property
    def mechanics(self):
        return self.__mechanics
    @mechanics.setter
    def mechanics(self, mechanics):
        self.__mechanics = mechanics

    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self, car):
        self.__car = car

