class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self, new_owner):
              self.owner = new_owner
              print(f"Owner updated. New vehicle owner of the {self.type} is {self.owner}")


car1 = Vehicle("D6978", "Tesla", "Daniela")
car2 = Vehicle("G1999", "GTR", "Gerardo")

car1.update_owner("Myron") # myron is my 6 month old son lol



print(f"Owner of car1: {car1.owner}")
print(f"Owner of car2: {car2.owner}")