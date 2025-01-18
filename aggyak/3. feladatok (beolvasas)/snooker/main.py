lista = []

with open("snooker.txt", "r", encoding="utf8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split(";")

            helyezes = int(sor[0])
            nev = sor[1]
            orszag = sor[2]
            nyeremeny = int(sor[3])
            lista.append([helyezes, nev, orszag, nyeremeny])


print(f"3. Feladat: A világranglistán {len(lista)} versenyző szerepel")

total_nyeremeny = sum([versenyzo[3] for versenyzo in lista])
atlag_nyeremeny = total_nyeremeny / len(lista)

print(f"4. Feladat: A versenyzők átlagosan {atlag_nyeremeny:.2f} fontot kerestek")

legjobb_versenyzo = None
max_nyeremeny = -1

for versenyzo in lista:
    if versenyzo[2] == 'Kína':
        if versenyzo[3] > max_nyeremeny:
            legjobb_versenyzo = versenyzo
            max_nyeremeny = versenyzo[3]

nyeremeny_font = legjobb_versenyzo[3]
nyeremeny_forint = nyeremeny_font * 380

nyeremeny_formazott = f"{nyeremeny_forint:,}".replace(",", " ")


print(f"5. Feladat: A legjobban kereső kínai versenyző: \n {sor[1]} \n helyezés: {sor[0]} \n ország: {sor[2]} \n nyeremény összege: {nyeremeny_formazott} Ft")

norveg_versenyzo = False

for jatekos in lista:
    if jatekos[2] == "Norvégia":  # Ellenőrizzük, hogy az ország a 3. elem
        norveg_versenyzo = True
        break  # Kilépünk a ciklusból, ha találtunk norvég versenyzőt

if norveg_versenyzo:
    print(f"6. Feladat: A versenyzők között van norvég versenyző.")
else:
    print(f"6. Feladat: A versenyzők között nincs norvég versenyző.")