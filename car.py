class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descname(self):
        long = f"{self.make} {self.model} {self.year}"
        return long.title()
    def read_odo(self):
        print(f"{self.odometer}")
    def up_odo(self, mil):
        if mil >=self.odometer:
            self.odometer = mil
        else:
            print("you can't roll")
    def inc_odo(self):
        self.odometer += mil

