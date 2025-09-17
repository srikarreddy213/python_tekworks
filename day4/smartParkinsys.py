class Vehicle:
    def __init__(self, nplate, oname):
        self.__nplate = nplate
        self.__oname = oname

    def calculate_parking_fee(self, vtype, hours):
        if vtype == "bike":
            bill = hours * 20
        elif vtype == "car":
            bill = hours * 50
        elif vtype == "suv":
            bill = hours * 70
        elif vtype == "truck":
            bill = hours * 100
        else:
            bill = 0
        print(f"The {vtype} stayed for {hours} hours and the bill is {bill} units.")

    def get_number_plate(self):
        return self.__nplate

    def get_owner_name(self):
        return self.__oname


class Bike(Vehicle):
    def __init__(self, nplate, oname, helmet_required):
        super().__init__(nplate, oname)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike Number Plate: {self.get_number_plate()}, Owner Name: {self.get_owner_name()}, Helmet Required: {self.helmet_required}")


class Car(Vehicle):
    def __init__(self, nplate, oname, seats):
        super().__init__(nplate, oname)
        self.seats = seats

    def display(self):
        print(f"Car Number Plate: {self.get_number_plate()}, Owner Name: {self.get_owner_name()}, Seats: {self.seats}")


class Suv(Vehicle):
    def __init__(self, nplate, oname, seats):
        super().__init__(nplate, oname)
        self.seats = seats

    def display(self):
        print(f"SUV Number Plate: {self.get_number_plate()}, Owner Name: {self.get_owner_name()}, Seats: {self.seats}")


class Truck(Vehicle):
    def __init__(self, nplate, oname, max_load_capacity):
        super().__init__(nplate, oname)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck Number Plate: {self.get_number_plate()}, Owner Name: {self.get_owner_name()}, Max Load Capacity: {self.max_load_capacity} kg")


