class shirts:
    def __init__(self,c,s,f,p,price):
        self.colour = c
        self.size = s
        self.fabric = f
        self.pattern = p
        self.price = price

s1=shirts("White","S","cotton","plain",600)
s2=shirts("Bule","M","denim","plain",800)
s3=shirts("Black","L","cotton","printed",1200)
s4=shirts("Green","XL","polyster","plain",900)
s5=shirts("Brown","M","cotton","checked",1300)

shirts_list = []
shirts_list.append(s1)
shirts_list.append(s2)
shirts_list.append(s3)
shirts_list.append(s4)
shirts_list.append(s5)

for obj in shirts_list:
    if obj.price < 1000:
        print(obj.colour,obj.size,obj.fabric,obj.pattern,obj.price)



