@staticmethod
def insert_str_info(prompt):
    data = input(prompt)
    if not isinstance(data, str) or data.isnumeric() or data.isdecimal():
        raise Exception("Nombre invalido!")
    return data

@staticmethod
def insert_number_info(prompt):
    data = input(prompt)
    if not data.isnumeric():
        raise Exception("Numero invalido!")
    return data

@staticmethod
def select_employee_type():
    print("Seleccione tipo de empleado:")
    print("1. Piloto")
    print("2. Piloto de Reserva")
    print("3. Mecanico")
    print("4. Jefe de equipo")
    entrada = input("Ingrese opcion: ")
    if entrada not in ["1", "2", "3", "4"]:
        raise Exception("Opcion invalida!")
    return int(entrada)

@staticmethod
def insert_nbr_list(prompt):
    nbrs = insert_str_info(prompt).split(",")
    for nbr in nbrs:
        if not nbr.isnumeric():
            raise Exception("Los numeros de autos deben ser numericos")
    return nbrs