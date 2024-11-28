mertekegyseg = input("Milyen mértékegységről szeretne átváltani? (liter/dl): ").lower()

szam = int(input("Adja meg az átváltandó mennyiséget: "))

if mertekegyseg == "liter":
    eredmeny = szam * 10
    print(f"{szam} liter {int(eredmeny)} = deciliter")
elif mertekegyseg == "dl":
    eredmeny = szam * 0.1
    print(f"{szam} deciliter = {int(eredmeny)} liter")
else:
    print("Hibás mértékegység. Kérlek, válassz 'liter' vagy 'deciliter' mértékegységet.")
