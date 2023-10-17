@staticmethod
def insert_str_info(promnt):
    data = input("Ingrese nombre: ")
    while not isinstance(data, str):
        print("Nombre invalido!")
        data = input(promnt)
    return data

@staticmethod
def insert_number_info(promnt):
    data = input(promnt)
    while not isinstance(data, int):
        print("Numero invalido!")
        data = input(promnt)
    return data

@staticmethod
def select_employee_type():
    print("Seleccione tipo de empleado:")
    print("1. Piloto")
    print("2. Mecanico")
    print("3. Jefe de equipo")
    entrada = input("Ingrese opcion: ")
    while entrada not in ["1", "2", "3"]:
        print("Opcion invalida!")
        entrada = input("Ingrese opcion: ")
    return int(entrada)