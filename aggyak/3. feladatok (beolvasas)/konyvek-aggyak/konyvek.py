konyvek = []

with open("konyvek.txt", "r", encoding="UTF8") as file:
    sorok = file.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        cím = sor[0]
        ar = int(sor[1])
        eladott = int(sor[2])
        ev = int(sor[3])

        konyvek.append([cím, ar, eladott, ev])

print("Könyvek listája: ")
for konyv in konyvek:
    print(f"{konyv[0]}, {konyv[1]}, {konyv[2]}, {konyv[3]}")
print("\n")


print("2010 után megjelent könyvek:")
for beolvas in konyvek:
     if beolvas[3] > 2010:
         print(f"{beolvas[0]}, {beolvas[1]}, {beolvas[2]}, {beolvas[3]}\n")

legolcsobb_konyv = konyvek[0]

for konyv in konyvek:
    if konyv[1] < legolcsobb_konyv[1]:
        legolcsobb_konyv = konyv

print(f"A legolcsóbb könyv: {legolcsobb_konyv[0]} {legolcsobb_konyv[1]} Ft\n")

print("Harry Potter könyvek kiírva a fájlba: ")
with open("HarryPotter_konyvek.txt", "w", encoding="UTF8") as fajl:
    for kiir in konyvek:
        if kiir[0].startswith("Harry Potter"):
            print(f"{kiir[0]}")
            fajl.write(f"{kiir[0]}\n")