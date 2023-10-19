from entidades.fia import Fia

def main_menu():
    print("\nBienvenido al programa de simulacion de carreras")
    print("Seleccione una opcion:")
    print("-----------------------------")
    print("1. Agregar Empleado")
    print("2. Agregar auto")
    print("3. Agregar Equipo")
    print("4. Simular carrera")
    print("5. Realizar consultas")
    print("6. Salir")
    entrada = input("Ingrese opcion: ")
    return entrada

def simulate_race():
    print("Simular carrera")
    fia.simulate_race()

def perform_queries():
    print("Realizar consultas")
    print("1. Top 10 conductores")
    print("2. Tabla de posiciones campeonato de constructores")
    print("3. Top 5 pilotos mejor pago")
    print("4. Top 3 pilotos mas habilidosos")
    print("5. Lista de jefes de equipo")
    entrada = input("Ingrese opcion: ")
    match entrada:
        case "1":
            fia.top_10_drivers()
        case "2":
            fia.constructors_table()
        case "3":
            fia.top_5_best_pay()
        case "4":
            fia.top_3_most_skilled()
        case "5":
            fia.team_principals()
        case _:
            print("Opcion invalida! Voliendo al menu principal")


if __name__ == '__main__':
    fia = Fia()
    while (entrada := main_menu()) != "6":
        try:
            match entrada:
                case "1":
                    if fia.add_team_employee():
                        print("Empleado agregado exitosamente!")
                case "2":
                    fia.add_car()
                case "3":
                    fia.add_team()
                case "4":
                    simulate_race()
                case "5":
                    perform_queries()
                case _:
                    print("Opcion invalida!")
        except Exception as e:
            print(e)
            print("Volviendo al menu principal...\n")
    print("Saliendo...")
