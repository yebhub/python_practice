class Car():

    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")



my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


class ElectricCar(Car): 

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery.")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()