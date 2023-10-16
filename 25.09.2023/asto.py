# uzdevums nr.2 - vairākiem nosacījumiem un funkciju, lambda

saraksts=[1,2,3,4,5,6,7,8,9,10] # masīvs

filtrets_saraksts=list(ilter(lambda x: x%2==0, saraksts))

print("Pāra skaitļi sarakstā: ", filtrets_saraksts)
