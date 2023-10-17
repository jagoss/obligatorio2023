from entidades.employee import Employee

class Driver(Employee):

    def __init__(self, ci, name, salary, age, country, score, car_nbr):
        super().__init__(ci, name, salary, age, country)
        self.__points = 0
        self.__score = score
        self.__car_nbr = car_nbr
    
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points):
        self.__points = points
    
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score
    
    @property
    def car_nbr(self):
        return self.__car_nbr
    @car_nbr.setter
    def car_nbr(self, car_nbr):
        self.__car_nbr = car_nbr