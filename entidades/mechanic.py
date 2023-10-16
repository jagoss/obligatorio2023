from entidades.employee import Employee

class Mechanic(Employee):

    def __init__(self, ci, name, salary, age, score):
        super().__init__(ci, name, salary, age)
        self.__score = score

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score