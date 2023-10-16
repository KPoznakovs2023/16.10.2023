# kā lietotājam ievadīt datus?
bums1=float(input("Ievadi 1. skaitli:"))
bums2=float(input("Ievadi 2. skaitli:"))
bums3=bums1*bums2
# 1.variants
print(f"Rezultāts ir {bums3}")
# 2.variants
rez="Rezultāts ir {}"
print(rez.format(bums3))
