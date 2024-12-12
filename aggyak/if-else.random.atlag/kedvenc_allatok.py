import random

allatok = []

print("Add meg az 3 kedvenc állatodat!")

while len(allatok) < 3:
    allat = input("Adj meg egy kedvenc állatot: ").lower()
    
    if allat not in allatok:
        allatok.append(allat)
        print(f"{len(allatok)} állat került hozzáadásra a listához.")
    else:
        print("Ez az állat már hozzá lett adva. Kérlek, adj meg egy másik állatot.")

print("\nA kedvenc állataid:")
print(", ".join(allatok))

valasztott_allat = random.choice(allatok)


print(f"\nA kiválasztott kedvenc állat: {valasztott_allat}")