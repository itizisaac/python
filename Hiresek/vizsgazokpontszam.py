# Kérje be a vizsgázók nevét és az elért pontszámokat! Írja meg azt a függvényt, ami eldönti, hogy a vizsga sikeres-e! A függvény paramétere a vizsgázó által elért pontszám, a visszatérési értéke logikai érték: igaz, ha a vizsga sikeres, hamis, ha sikertelen. Ezt a függvényt használja fel a programjában!

# A program kérdezgesse addig újabb és újabb vizsgázó nevét és pontszámát, amíg a vizsgázó nevének megadásakor üres bemenetet nem kap! Ilyen akkor történik, ha a felhasználó egyszerűen Entert nyom, anélkül hogy bármit is begépelne.

# A program üzeneteinek megfogalmazásában kövesse az alábbi példát! Azokat a részeket, amiket a felhasználó gépel be, a mintában vastagított és döntött betűkkel emeltük ki.

def vizsga(pont):
    return pont >=48

while True:
    nev = input("Add meg a vizsgázó nevét!")
    if nev == "":
        break
    pontszam = int(input("Add meg a pontszámát!"))

    if vizsga(pontszam):
        print(f"{nev} vizsgája sikeres.")
    else:
        print(f"{nev} vizsgája sikertelen.")
