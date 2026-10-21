class Car:
    def __init__(self,b,c,f_t,p):
        self.brand = b
        self.colour = c
        self.fuel_type = f_t
        self.price = p

C1 = Car("Mahindra","Black","diesel",1500000)
C2 = Car("Toyota","Black","petrol",5100000)
C3 = Car("Maruri","White","CNG",1200000)
C4 = Car("Tata","White","petrol",900000)
C5 = Car("Hyundai","Blue","diesel",1100000)

Car_list = []
Car_list.append(C1)
Car_list.append(C2)
Car_list.append(C3)
Car_list.append(C4)
Car_list.append(C5)


for obj in Car_list:
    if obj.fuel_type == "diesel":
        print(obj.brand,obj.colour,obj.fuel_type,obj.price)