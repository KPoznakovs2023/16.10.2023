# uzdevums nr.1 - vairākiem nosacījumiem un funkciju, lambda

def izvele_skaitlim(skaitlis):
    # parametrs ir mainīgais, kurš strādā funkcijas ietvaros
    darbiba={
        "a": lambda x: x**2,
        "b": lambda x: x**3,
        "c": lambda x: x*2,
    }
    if skaitlis>10:
        rezultats=darbiba["a"]
    elif skaitlis<-10:
        rezultats=darbiba["b"](skaitlis)
    else:
        rezultats=darbiba["c"](skaitlis)
    return rezultats
rez=izvele_skaitlim(11)
print(rez)