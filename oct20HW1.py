class Mobile:
    def __init__(self,b,c,m,r,s,p):
        self.brand = b
        self.colour = c
        self.model = m
        self.ram = r
        self.storage = s
        self.price = p

M1=Mobile("Apple","white","iphone","16GB","512GB",80000)
M2=Mobile("Motorola","Blue","Edge60 stylus","8GB","256GB",25000)
M3=Mobile("samsung","Lavender","galaxyA36 5G","8GB","256GB",36000)
M4=Mobile("Realme","green","P3 5G","8GB","128GB",17000)
M5=Mobile("Vivo","Blue","V80","16GB","256GB",58000)

Mobile_list=[]
Mobile_list.append(M1)
Mobile_list.append(M2)
Mobile_list.append(M3)
Mobile_list.append(M4)
Mobile_list.append(M5)
Mobile_list.append(M1)

for obj in Mobile_list:
    if obj.price >50000:
        print(obj.brand,obj.colour,obj.model,obj.ram,obj.storage,obj.price)

