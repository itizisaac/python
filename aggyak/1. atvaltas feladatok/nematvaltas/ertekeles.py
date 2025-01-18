etel = input("Étel neve: ")
rendelo = input("Étel rendelejőnek neve: ")
ertkeles = int(input("Értékelés (1-5): "))


if ertkeles <= 0:
    print("Az értékelés nem lehet negatív!")
elif ertkeles > 5:
    print("5 pont feletti értékelés nem elfogatható!")
else:
    print("Köszönjük az értékelést!")