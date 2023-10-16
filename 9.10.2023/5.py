# Izvadiet  saitļus no 1 lidz 100, bet katru reizi,
#kad sasniedzat skaitli, kas dalas ar 3, izvadiet "Fizz"
#un katru reizi, kad sasniedzat sakitli, kas dalas ar 5, ievadiet "Buzz"
#Jā skaitlis  dalas gan ar 3, gan ar 5, izvadiet "FizzBuzz"

for skaitlis in range(1, 101):
    if skaitlis %3==0 and skaitlis%5==3:
        print("FizzBuzz")
    elif skaitlis%3==0:
          print("Fizz")
    elif skaitlis%3==0:
          print("Buzz")
    else:
          print("skaitlis")