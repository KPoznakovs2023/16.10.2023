# Cikla konstrukcijas

# 1.For cikls ***iterācija***
saraksts=[1,2,3,4,5]
for elements  in saraksts:
    print(elements)
# 2. Cikls for, apstrādājot veselu skaitļu intervālu
#Intervāla norādīšanai tiek izmantotankcija range.
a=int(input("Ievadiet skaitli: "))
s=0
for i in range(1, a+1):
    s+=i
print(s)
