# Lietotajs ievada tekstu un apreķiniet burtu un vardu skaitu taja.

# Lietotaja ievaditais teksts
teksts=input("Ievadiet tekstu: ")

# Apreķinat burtu skaitu ...k programma zinas ka tas ir burts? %aka
# isaplpha()
burtuskaits=0
for bursts in teksts:
    if bursts.isaplha():
        burtuskaits+=1 # nozime ka burtuskaits=burtuskaits+1



# sadalit tekstu pa vardiem
vardi=teksts.split()  # atdalitajs split(",")

# apreķinat vardu skaitu

# izvadit rezultatu
print(f"Burtu skaits ir {burtuskaits}")
print(f"Vardu skaits")