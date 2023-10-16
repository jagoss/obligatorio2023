from entidades.employee import Employee

class Driver(Employee):
    
    def __init__(self, ci, name, salary, age, nro, points, score):
        super().__init__(ci, name, salary, age)
        self.__nro = nro
        self.__points = points
        self.__score = score
    
    @property
    def nro(self):
        return self.__nro
    @nro.setter
    def nro(self, nro):
        self.__nro = nro
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