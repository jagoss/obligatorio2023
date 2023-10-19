from entidades.team import Team
from entidades.driver import Driver


class Race:
    def __init__(self, teams) -> None:
        self.__teams: list[Team]  = teams      
        self.__drivers_out = []
        self.__penalized_drivers = []
        self.__pit_error_drivers = []
    
    def add_driver_out(self, driver_nbr):
        try:
            driver = self.__find_driver(driver_nbr)
            self.__drivers_out.append(driver)
            print(f"El conductor {driver.name} abanda de la carrera!")
        except Exception as e:
            print(e.args[0])

    def add_penlized_driver(self, driver_nbr):
        try:
            driver = self.__find_driver(driver_nbr)
            self.__penalized_drivers.append(driver)
            print(f"El conductor {driver.name} fue penalizado!")
        except Exception as e:
            print(e.args[0])

    def add_pit_error_driver(self, driver_nbr):
        try:
            driver = self.__find_driver(driver_nbr)
            self.__pit_error_drivers.append(driver)
            print(f"El conductor {driver.name} tuve un error en los pits!")
        except Exception as e:
            print(e.args[0])

    def simulate(self) -> list[Driver]:
        result = []
        for team in self.__teams:
            if len(team.mechanics) > 0:
                for driver in team.drivers:
                    driver_to_add = driver if not driver.injured and team.reserve_driver not in result else team.reserve_driver
                    driver_to_add.race_score = self.__race_score(driver_to_add, team)
                    result.append(driver_to_add)
        result.sort(key=lambda x: x.race_score, reverse=True)
        return result

    def __race_score(self, driver, team):
        score = 0
        if driver not in self.__drivers_out:
            score = driver.score + team.car.score + sum([mechanic.score() for mechanic in team.mechanics]) - 8*self.__penalized_drivers.count(driver) - 5*self.__pit_error_drivers.count(driver)
        return score
                    
    
    def __find_driver(self, driver_nbr):
        driver = None
        for team in self.__teams:
            driver = [driver for driver in team.drivers if driver.nbr == driver_nbr][0]
            if driver is not None:
                break
        if driver is None:
            raise Exception(f"El conductor {driver_nbr} no existe")
        return driver