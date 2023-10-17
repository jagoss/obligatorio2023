from entidades.fia import Fia


def main_menu():
    print("\nBienvenido al programa de simulacion de carreras")
    print("Seleccione una opcion:")
    print("-----------------------------")
    print("1. Agregar Empleado")
    print("2. Agregar Equipo")
    print("3. Simular carrera")
    print("4. Realizar consultas")
    print("5. Salir")
    entrada = input("Ingrese opcion: ")
    return entrada

def add_team():
    print("Agregar Equipo")

def simulate_race():
    print("Simular carrera")

def perform_queries():
    print("Realizar consultas")

if __name__ == '__main__':
    fia = Fia()
    while (entrada := main_menu()) != "5":
        match entrada:
            case "1":
                if fia.add_team_employee():
                    print("Empleado agregado exitosamente!")
            case "2":
                add_team()
            case "3":
                simulate_race()
            case "4":
                perform_queries()
            case _:
                print("Opcion invalida!")
    print("Saliendo...")
