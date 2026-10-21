class fruit:
    def __init__(self,n,c,s,t,season,):
        self.name = n
        self.colour = c
        self.shape = s
        self.taste = t
        self.season = season

f1=fruit("apple","red","round","sweet","autumn")
f2=fruit("banana","yellow","curved","sweet","all season")
f3=fruit("mango","yellow","oval","sweet","summer")
f4=fruit("orange","orange","round","sweet and sour","winter")
f5=fruit("strawberry","red","heard-shaped","sweet and sour","winter")

fruit_list = []
fruit_list.append(f1)
fruit_list.append(f2)
fruit_list.append(f3)
fruit_list.append(f4)
fruit_list.append(f5)

for obj in fruit_list:
    if obj.taste == "sweet":
        print (obj.name,obj.taste)