# Cikla konstrukcijas

# 1.For cikls ***iterācija***
# 2. Cikls for, apstrādājot veselu skaitļu intervālu
#Intervāla norādīšanai tiek izmantotankcija range.
# 3. Cikls for, apstrādājot elementu kopumu.
# 4. Cikls ar priekšnosacījumu while
#While cikls izpildīs ciklu, kamēr dotā nosacījums ir patiss.
# Cikla pārtraukšana un turināšana !!!
saraksts=[1,2,3,4,5,]
for elements in saraksts:
    if elements==3:
        continue # Pārtrauca šo iterāciju un turpinnāmar nākošo!
    if elements==5:
        break # Iziet no cikla, ja elements ir 5
    print(elements)