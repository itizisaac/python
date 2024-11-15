# 1.Feladat
# Olvassuk be az atlag.txt fájlt, írjuk ki a lista teljes tartalmát. Számoljuk ki az átlagot,kerekítsük 2 tizedesjegyre.
# Írjuk ki azoknak a neveit és átlagát akiknek K-val kezdődik a nevük.

lista = []
atlagok = []

with open("atlag.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        adat = line.split(";")
        
        nev = adat[0]
        atlag = float(adat[1])
        lista.append([nev,atlag])

for item in lista:
    #print(f"{item[0]}; {item[1]}")
    atlagok.append(item[1])
    if item[0].startswith("T"):
        print(f"{item[0]},{item[1]}")



print(f"Az osztály átlaga {round(sum(atlagok)/len(atlagok), 2)}")