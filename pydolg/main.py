# 1.Feladat
# Kérj be egy szót a felhasználótól, és vizsgáld meg, hogy valamelyik szóban van-e s vagy c.

szo = input("Adj meg egy szót: ")

if "s" in szo and "c" in szo:
    print("A szóban van c és s betű is.")
elif "s" in szo:
    print("A szóban s betű van")
elif "c" in szo:
    print("A szóban c betű van")
else:
    print("A szóban egyik betű sem szerepel.")


# 2.Feladat
# A megkapott listához, adj hozzá még egy szót, és addig kell a bekérni a felhasználótól, amíg nem lesz hosszabb, mint 3 betűs. Majd írd ki, hogy melyik szó lett hozzáadva a listához,
# és azoknak a szavak db számát amik t-vel kezdődnek és írd ki pontos vesszővel elválasztva a t-vel kezdődő szavakat

szavak = ["A", "nap", "ragyog", "az", "égen", "és", "a", "madarak", "vidáman", "csiripelnek", "a", "fákon", "amíg", "az", "emberek", "sétálnak", "a", "parkban", "és", "élvezik", "a", "szép", "időt", "tavasz", "tarka", "tulipánok", "tündökölnek"]

db = 0

while True:
    szok = input("Adj meg egy szót! ")
    if len(szok) > 3:
         
         szavak.append(szok)
         print(f"A listához adott szó: {szok}")
         break
    else:
         print("A szónak hosszabbnak kell lennie, mint 3 betű.")

for i in szavak: 
    if i.startswith("t"):
            db += 1
            
print(f"A listában {db} db t-vel kezdődő szó van.")

tbetus = []

tbetus.append(db)

print(f"A t-vel kezdődő szavak: {';'.join(map(str,tbetus))}")

# # 3.Feladat
# # Olvasd be és tárold el az ajandek lista tartalmát. Írask ki a lista teljes tartalmát. A legfiatalabb személynek írd ki a nevét és korát. 
# # Írd ki, hány db kategória van a listában, ismétlés nélkül. Jelenítsd meg a konzolon a személyek neveit, az összeget és akciós árakat, mindenkinél egységesen 20% a kedvezmény.
# # Írasd ki szbetuvelkezd.txt fájlba, egymás alá rendezve, az Sz-el kezdődő neveket.

lista = []

kategoriak = []

legfiatalabb = 0
legfiatalabbSzemely = ""

with open("ajandek.txt", "r", encoding="UTF8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split(";")

            nev = sor[0]
            termeknev =sor[1]
            ar = int(sor[2])
            szuletesi_ev = int(sor[3])
            kategoria = sor[4]

            lista.append([nev, termeknev, ar, szuletesi_ev, kategoria])

for item in lista:
    if item[3] > legfiatalabb:
         legfiatalabb = item[3]
         legfiatalabbSzemely = item[0]

    if item[4] not in kategoriak:
        kategoriak.append(item[4])

    akcios_ar = item[2] * (0.8)
    print(f"{item[0]} Eredeti ár: {item[2]} Ft | Akciós ár: {akcios_ar}")

print(f"Kategóriák száma: {len(kategoriak)}")
print(f"A legfiatalabb személy: {legfiatalabbSzemely}, {legfiatalabb}")

szbetus_nevek = []

for item in lista:
    if item[0].startswith("Sz"):
        szbetus_nevek.append(item[0])

with open("szbetuvelkezd.txt", "w", encoding="UTF8") as fajl:
    for nev in szbetus_nevek:
        fajl.write(nev + "\n")