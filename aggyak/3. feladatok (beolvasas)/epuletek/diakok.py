from datetime import datetime

# 2.Feladat
# Olvassuk be a diakok.txt listát, írjuk ki a teljes tartalmát, mentsük el txt fájlban külön a telefonszámokat és nézzük meg ki a legfiatalabb.

lista = []

yettel = []
telekom = []
vodafone = []

legfiatalabb = datetime.min
legfiatalabbNev = None

with open("diakok.txt", "r", encoding="UTF8") as file:
    lines = file.readlines()

    for line in lines[1:]:
        line = line.strip()
        adat = line.split(";")


        nev = adat[0]
        atlag = float(adat[1])
        tel = adat[2]
        szuletesi = datetime.strptime(adat[3], "%Y-%m-%d")
        lista.append([nev, atlag, tel, szuletesi])

for item in lista:
    #print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")
    if item[3] > legfiatalabb:
        legfiatalabb = item[3]
        legfiatalabbNev = item[0]
    if item[2].startswith("+3620"):
        yettel.append(item[0])
    elif item[2].startswith("+3630"):
        telekom.append(item[0])
    elif item[2].startswith("+3670"):
        vodafone.append(item[0])
        

print(f"A legfiatalabb: {legfiatalabbNev}, {legfiatalabb}")

with open("szolgaltatok.txt", "w", encoding="UTF8") as fajl:
    fajl.write("20-as telefonszámok \n")
    for y in yettel:
        for list in lista:
            if y == list[0]:
                fajl.write(f"\n{y}, {list[2]}")
    fajl.write("\n")
    fajl.write("30-as telefonszámok \n")
    for t in telekom:
        for list in lista:
            if t == list[0]:
                fajl.write(f"\n{t}, {list[2]}")
    fajl.write("\n")
    fajl.write("70-es telefonszámok \n")
    for v in vodafone:
        for list in lista:
            if v == list[0]:
                fajl.write(f"\n{v}, {list[2]}")