class soap:
    def __init__(self,n,c,f,s,p):
        self.name = n
        self.colour = c
        self.fragrance = f
        self.shap = s
        self.price = p

s1=soap("Lux","pink","rose","oval","40")
s2=soap("Santoor","orange","sndalwood","rectangular","35")
s3=soap("Dove","white","creamy","oval","65")
s4=soap("Cinthol","green","freshlime","rectangular","40")
s5=soap("Dettol","cream","antiseptic","rectangular","45")

soap_list = []
soap_list.append(s1)
soap_list.append(s2)
soap_list.append(s3)
soap_list.append(s4)
soap_list.append(s5)

for obj in soap_list:
    if obj.shap == "rectangular":
        print(obj.name,obj.colour,obj.fragrance,obj.shap,obj.price)

