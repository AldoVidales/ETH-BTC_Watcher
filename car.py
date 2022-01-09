class Car:
    """A simple attemp to represent a car"""

    def __init__(self,make,model,year):
        self.make = make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=f"{self.year}{self.make}{self.model}"
        return long_name

    def get_matricule(self):
        matricule="34454323"
        return matricule


class Electricalcar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)



my_new_car=Car('audi ','a4 ','2019 ')
print(f"{my_new_car.get_descriptive_name()} , matricule: {my_new_car.get_matricule()}")
my_tesla=Electricalcar(' tesla',' model s', 2019)
print(my_tesla.get_descriptive_name())