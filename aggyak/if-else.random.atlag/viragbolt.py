viragok = []

with open('viragok.txt', 'r', encoding='UTF8') as file:
    sorok = file.readlines()

    for sor in sorok:
        sor = sor.strip()
        adat = sor.split(", ")
        viragok.append([adat[0], float(adat[1]), int(adat[2]), adat[3]])

print("A fájl tartalma:")
for virag in viragok:
    print(f"{virag[0]}, {virag[1]} Ft, {virag[2]} darab, Szállítás: {virag[3]}")

legdragabb = viragok[0]
for virag in viragok:
    if virag[1] > legdragabb[1]:
        legdragabb = virag
print(f"\nA legdrágább virág: {legdragabb[0]} - {legdragabb[1]} Ft")

db = 0
for virag in viragok:
    db += virag[2]
atlag = db / len(viragok)
print(f"Az eladott virágok átlagos darabszáma: {atlag:.0f} darab")

r_viragok = []

for virag in viragok:
    if virag[0].lower().startswith('r'):
        r_viragok.append(virag)
print(f"\nA 'R'-rel kezdődő virágok száma: {len(r_viragok)}")

print("\nA 'R'-rel kezdődő virágok:")
for virag in r_viragok:
    print(f"{virag[0]}, {virag[1]} Ft, {virag[2]} darab, Szállítás: {virag[3]}")

with open('R_betus_viragok.txt', 'w', encoding='UTF8') as file:
    for virag in r_viragok:
        file.write(f"{virag[0]}, {virag[1]} Ft, {virag[2]} darab, Szállítás: {virag[3]}\n")
