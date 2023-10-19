from entidades.employee import Employee

class Driver(Employee):

    def __init__(self, ci, name, salary, age, country, score, car_nbr):
        super().__init__(ci, name, salary, age, country)
        self.__points = 0
        self.__score = score
        self.__car_nbr = car_nbr
        self.__injured = False
        self.__race_score = 0
    
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

    @property
    def race_score(self):
        return self.__race_score
    @race_score.setter
    def race_score(self, race_score):
        race_score = race_score
    
    @property
    def injured(self):
        return self.__injured
    @injured.setter
    def injured(self, injured):
        self.__injured = injured

    def add_points(self, pos):
        match pos:
            case 1:
                self.points += 25
            case 2:
                self.points += 18
            case 3:
                self.points += 15
            case 4:
                self.points += 12
            case 5:
                self.points += 10
            case 6: 
                self.points += 8
            case 7:
                self.points += 6
            case 8:  
                self.points += 4
            case 9:
                self.points += 2
            case 10:
                self.points += 1  
            case _:
                self.points += 0