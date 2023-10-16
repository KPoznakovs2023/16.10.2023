# Cikla konstrukcijas

# 1.For cikls ***iterācija***
# 2. Cikls for, apstrādājot veselu skaitļu intervālu
#Intervāla norādīšanai tiek izmantotankcija range.
# 3. Cikls for, apstrādājot elementu kopumu.
# 4. Cikls ar priekšnosacījumu while
#While cikls izpildīs ciklu, kamēr dotā nosacījums ir patiss.
# Cikla pārtraukšana un turināšana !!!
# Enumerate cikls
sarakts=['a', 'b', 'c']
# uzdevums -
# uzdevums - izdrukāt visus pāra skaitļus robežās no 10 līdz 100, galapunktus ieskaitot!
# 1. risinājums
for skaitlis in range(10, 101):
    if  skaitlis %  2==0:
         print(skaitlis)
# 2. risinājums
for skaitlis in range(10,101,2):
    print(skaitlis)

