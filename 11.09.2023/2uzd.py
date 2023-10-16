"""
1.piemērs
a=25
b=0.35
# izvadīt terminālu, kurā ir iekļauti mainīgo vērtības!
print("Eimija nopirka", a, "saldējumus.")

# 2.piemers
vards=Eimija
vecums=4
# Izmantojot f-string (sākot ar Python 3.6+)
print(f"Mani sauc {vards} un man ir {vecums} gadi.")

# 3.piemers
# Izmantojot format mtodi
vards="Eimija"
vecums=4
zinama_virkne="Mani sauc {} un man ir {} gadi."
print(zinama_virkne.format(vards,vecums))
"""
#4.piemers
#Izmantojot % operātoru (vecais vids, taču tas joprojām darbojas)
vards = "Anna"
vecums = 30

zinama_virkne = "Mani sauc %s un man ir %d gadi." % (vards, vecums)
print(zinama_virkne)

