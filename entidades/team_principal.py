from entidades.employee import Employee

class TeamPrincipal(Employee):
    def __init__(self, ci, name, salary, age):
        super().__init__(ci, name, salary, age)