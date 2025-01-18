muveszbolt = []
darabszam = []
c_betus = []

legdrabbtermekar = 0
legdrabbnev = None

with open("termekek.txt", "r", encoding="utf-8") as file:
    sorok = file.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        nev = sor[0]
        ar = int(sor[1])
        eladott = int(sor[2])
        ev = int(sor[3])

        muveszbolt.append((nev, ar, eladott, ev))

        if ar > legdrabbtermekar:
            legdrabbtermekar = ar
            legdrabbnev = nev

        darabszam.append(eladott)

print("A fájl tartalma:")
for muvesz in muveszbolt:
    print(f"{muvesz[0]}, {muvesz[1]}, {muvesz[2]}, {muvesz[3]}")

print(f"A legdrágább termék:  {legdrabbnev} {legdrabbtermekar} Ft")

if darabszam:
    atlag = sum(darabszam) / len(darabszam)
    print(f"Az eladott termékek darabszámának átlaga: {round(atlag)}")
else:
    print("Nincsenek eladott termékek.")

for c in muveszbolt:
    if c[0].startswith("C"):
        c_betus.append(c)

print(f'"C"-vel kezdődő termékek száma: {len(c_betus)}')

print('"C"-vel kezdődő termékek: ')
with open("C_betus_termekek.txt", "w", encoding="utf-8") as fajl:
    fajl.write('"C"-vel kezdődő termékek: \n')
    for kiir in muveszbolt:
        if kiir[0].startswith("C"):
            print(f"{kiir[0]}, {kiir[1]}, {kiir[2]}, {kiir[3]}")
            fajl.write(f"{kiir[0]}, {kiir[1]}, {kiir[2]}, {kiir[3]} \n")