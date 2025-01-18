lista = []

pontszamok = []

with open("fifa.txt", "r", encoding="utf8") as fajl:
    sorok = fajl.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        csapat = sor[0]
        helyezes = int(sor[1])
        valtozas = int(sor[2])
        pontszam = int(sor[3])
        lista.append([csapat, helyezes, valtozas, pontszam])
        pontszamok.append(pontszam)

print(f"3. feladat: A világranglistán {len(lista)} csapat szerepel")

atlag_pontszam = sum(pontszamok) / len(pontszamok)
print(f"4. feladat: A csapatok átlagos pontszáma: {atlag_pontszam}")

max_valtozas = lista[0]

for csapat in lista:
    if csapat[2] > max_valtozas[2]:
        max_valtozas = csapat

print(f"5. feladat: A legtöbbet javító csapat")
print(f"Csapat neve: {max_valtozas[0]}")
print(f"Hellyezés: {max_valtozas[1]}")
print(f"Változás: {max_valtozas[2]}")
print(f"Pontszám: {max_valtozas[3]}")

#6.feladat
if sor[0].startswith("Magyarország"):
    print("6. Feladat: A csapatok között van Magyarország.")
else:
    print("6. Feladat: A csapatok között nincs Magyarország.")

# 7. feladat: Statisztika
valtozas_stat = {}

for csapat in lista:
    valtozas = csapat[2]
    if valtozas in valtozas_stat:
        valtozas_stat[valtozas] += 1
    else:
        valtozas_stat[valtozas] = 1

print(f"7. feladat: Statisztika")
for valtozas, count in valtozas_stat.items():
    if count > 1:
        print(f"{valtozas} helyett változott: {count} csapat")