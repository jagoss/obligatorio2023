class Car:
    def __init__(self, model, year, score):
        self.model = model
        self.year = year
        self.scrore = score

    def drive(self):
        print("Driving the car")

    def stop(self):
        print("Stopping the car")

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Car):
            return False
        return self.model == __value.model

    def __str__(self):
        return f"Model: {self.model}, Color: {self.color}, Year: {self.year}"