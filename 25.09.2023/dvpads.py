# uzdevums nr.6 - vairākiem nosacījumiem un funkciju, lambda

def validet_vardu(vards):
    if len(vards) <3:
        return "Vārds ir pārāk īss"
    elif len (vards)>20
        return "Vārds pārāk garš"
    elif not vards.isalpha(): #Ivo2
        return "Vārds drīkst saturēt tik burtus!"
    else:
        return "Vārds ir derīgs!"


ievade=input("Ievadi savu vārdu: ")
rezultats=validet_vardu(ievade)
print(rezultats)