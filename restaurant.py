class Restaurant():

    def __init__(self, name, cusine_type):
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0 

    def decribe_restaurant(self):
        print(self.name.title() + " serves " + self.cusine_type + " food.")


    def open_restaurant(self):
        print(self.name.title() + " is now open!!")

    def set_number_served(self, served_customers):
        self.number_served = served_customers

    def increment_number_served(self, served_customers):
        self.number_served += served_customers



restaurant = Restaurant("Dennys", "americana diner")

restaurant.decribe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(12)
print(restaurant.number_served)
restaurant.increment_number_served(12)
print(restaurant.number_served)