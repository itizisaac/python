zoldsegek = []

paprika = []

with open("zoldsegek.txt", "r", encoding="UTF8") as file:
    for line in file:
        zoldsegek.append(line.strip())

print("A teljes fájl tartalma:")
for zoldseg in zoldsegek:
    reszek = zoldseg.split(';') 
    nev = reszek[0]
    tonna = int(reszek[1])
    ftkg = int(reszek[2])
    ev = int(reszek[3])

    print(f"{nev} - {tonna} tonna - {ftkg} Ft/kg - {ev}")

print("\n2015 utáni zöldségek:")
for zoldseg in zoldsegek:
    reszek = zoldseg.split(';')
    ev = int(reszek[3])
    if ev > 2015:
        print(f"{reszek[0]} - {reszek[1]} tonna - {reszek[2]} Ft/kg - {reszek[3]}")

legolcsobb_zoldseg = zoldsegek[0]
for zoldseg in zoldsegek:
    reszek = zoldseg.split(';')
    if int(reszek[2]) < int(legolcsobb_zoldseg.split(';')[2]):
        legolcsobb_zoldseg = zoldseg

reszek = legolcsobb_zoldseg.split(';')
print(f"\nA legolcsóbb zöldség:\n{reszek[0]} - {reszek[2]} Ft/kg")

for zoldseg in zoldsegek:
    reszek = zoldseg.split(';')
    if reszek[0].startswith("Paprika"):
        paprika.append(zoldseg)

print(f"\n'Paprika'-val kezdődő zöldségek száma: {len(paprika)}")
print("\nEzek a zöldségek 'paprika'-val kezdődnek:")
for zoldseg in paprika:
    reszek = zoldseg.split(';')
    print(f"{reszek[0]} - {reszek[1]} tonna - {reszek[2]} Ft/kg - {reszek[3]}")

with open("paprika_zoldsegek.txt", "w", encoding="UTF8") as fajl:
    for zoldseg in paprika:
        fajl.write(f"{zoldseg}\n")

print("\nA paprika_zoldsegek.txt fájlba kiírásra kerültek az adatok.")
