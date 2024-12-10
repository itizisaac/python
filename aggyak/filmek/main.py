lista = []

with open("film.txt", "r", encoding="UTF8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split(";")

            cím = sor[0]
            rendezo =sor[1]
            foszereplo = sor[2]
            ev = int(sor[3])
            perc = int(sor[4])

            lista.append([cím, rendezo, foszereplo, ev, perc])


legrovidebbfilm = ""
legrovidebbcim = float("inf")

for film in lista:
      hossz = len(film[0])
      if hossz < legrovidebbcim:
            legrovidebbcim = len(film[0])
            legrovidebbfilm = film[0]

print(legrovidebbfilm)


perces_filmek = 0
for film in lista:
    if film[4] >= 110:
        perces_filmek += 1

print(perces_filmek)

szinesz = input("Adj meg egy színész nevet: ").strip()

with open("ajanlottfilmek.txt", "w", encoding="UTF8") as fajl:
    for film in lista:
        if szinesz == film[2]:
            fajl.write(f"Ajánlott film: {film[0]} ({film[3]})\n")
            break
    else:
         fajl.write("Nincs ilyen színész.\n")

rendezok_stat = {}

for film in lista:
    rendezo = film[1]
    if rendezo in rendezok_stat:
        rendezok_stat[rendezo] += 1
    else:
        rendezok_stat[rendezo] = 1

with open("rendezok_stat.txt", "w", encoding="UTF8") as stat_fajl:
    for rendezo, film_szam in rendezok_stat.items():
        stat_fajl.write(f"{rendezo}: {film_szam} film\n")

print("A rendezők statisztikája a 'rendezok_stat.txt' fájlba lett írva.")