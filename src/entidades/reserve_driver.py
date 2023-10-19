from entidades.driver import Driver

class ReserveDriver(Driver):
    def __init__(self, ci, name, salary, age, country, score, car_nbr):
        super().__init__(ci, name, salary, age, country, score, car_nbr)