class Team:
    def __init__(self, name, constructor_points, score) -> None:
        self.__name = name
        self.__constructor_points = constructor_points
        self.__score = score
        self.__drivers = []
        self.__team_principal = None
        self.__mechanics = []
        self.__car = None

    @property
    def name(self):
        return self.__name
    
    @name.setter   
    def name(self, name):
        self.__name = name
    
    @property
    def constructor_points(self):
        return self.__constructor_points
    
    @constructor_points.setter
    def constructor_points(self, constructor_points):
        self.__constructor_points = constructor_points
    
    @property
    def score(self):  
        return self.__score
    
    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def drivers(self):
        return self.__drivers
    
    @drivers.setter
    def drivers(self, drivers):
        self.__drivers = drivers

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

