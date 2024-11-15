mertekegyseg = input("Milyen mértékegységben adod meg? (MB/GB): ").upper()
atvaltando = int(input("Írd be az átváltandó számot: "))


if mertekegyseg == "MB":
    eredmeny = atvaltando / 1024
    print(f"Az eredmény: {eredmeny} GB")
elif mertekegyseg == "GB":
    eredmeny = atvaltando * 1024
    print(f"Az eredmény: {eredmeny} MB")
else:
    print("Ismeretlen mértékegység.")


