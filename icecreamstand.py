from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, name, flavors, cuisine_type="Ice Cream"):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(self.name.title() + " serves the following flavors: ")

        for flavor in self.flavors: 
            print(flavor.title())


baskin = IceCreamStand("Baskin Robins", ["strawberry", "chocolate", "vanilla", "rocky road"])

baskin.display_flavors()