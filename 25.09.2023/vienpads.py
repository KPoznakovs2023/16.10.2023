# uzdevums nr.5 - vairākiem nosacījumiem un funkciju, lambda


"""
Lietotajs ievada 2 skaitļus, jāizveido programma, kas šos skaitļus salīdzina,
izveidojot funkciju ar diviem parametriem.
"""

def noteikt_skaitlus(skaitlis1, skaitlis2):
    if skaitlis1>0 and skaitlis2>0:
    return "Abi skaitļi ir pozītivi"
elif skaitlis1<0 and skaitlis2<0:
    return "Abi skaitļi ir negatīvi"
elif skaitlis1==0 or skaitlis2==0:
    return "Vismaz viens skaitlis ir nulle"
else:
    return "Skaitļi ir ar dažādām zīmēm..."

sk1=int(input("Ievadi 1. skaitli:"))
sk2=int(input("Ievadi 2. skaitli:"))
rezultats=noteikt_skaitlus(sk1,sk2)
print(rezultas)
