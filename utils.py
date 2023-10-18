@staticmethod
def insert_str_info(prompt):
    data = input("Ingrese nombre: ")
    while not isinstance(data, str):
        print("Nombre invalido!")
        data = input(prompt)
    return data

@staticmethod
def insert_number_info(prompt):
    data = input(prompt)
    while not isinstance(data, int):
        print("Numero invalido!")
        data = input(prompt)
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

@staticmethod
def insert_nbr_list(prompt):
    nbrs = insert_str_info(prompt).split(",")
    for nbr in nbrs:
        if not nbr.isnumeric():
            raise Exception("Los numeros de autos deben ser numericos")
    return nbrs