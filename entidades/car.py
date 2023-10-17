class Car:
    def __init__(self, model, color, year, score):
        self.model = model
        self.color = color
        self.year = year
        self.scrore = score

    def drive(self):
        print("Driving the car")

    def stop(self):
        print("Stopping the car")

    def __str__(self):
        return f"Model: {self.model}, Color: {self.color}, Year: {self.year}"