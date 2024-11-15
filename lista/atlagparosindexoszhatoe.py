"""
1. Feladat
Számoljuk meg a pontszámok átlagát és írjuk ki a konzolra.
Növekvő sorrendbe írjuk ki a pontszámokat.
"""
print('1. Feladat')

pontszamok = [
    95, 78, 84, 62, 47, 88, 93, 71, 56, 82,
    65, 90, 74, 60, 85, 79, 68, 91, 73, 58,
    100, 81, 77, 66, 49, 53, 69, 94, 87, 61,
    80, 55, 76, 67, 48, 86, 92, 72, 59, 83,
    64, 50, 99, 75, 89, 54, 63, 57, 70, 52
]

print(f"A pontszámok átlaga: {sum(pontszamok) / len(pontszamok)}")

pontszamok.sort()
print(pontszamok)

"""
2.Feladat
Úgy írjuk ki a lista tartalmát, hogy csak a páros indexű szavak kerüljenek kiírásra a konzolon, 
vesszővel elválasztva.
"""

print('2. Feladat')

oszi_szavak = [
    "falevél", "szüret", "tök", "gesztenye", "sárgulás",
    "hűvös", "szél", "eső", "kabát", "sapka",
    "melegítő", "forrócsoki", "köd", "erdei séta", "makk",
    "szőlő", "almabor", "kandalló", "tábortűz", "sál",
    "esernyő", "sütemény", "krumplisütés", "párolgás", "fénycsökkenés",
    "avartakaró", "madárvonulás", "barnulás", "hosszú esték", "kézművesség",
    "sütőtök", "árnyék", "gomba", "séta", "kuckózás",
    "termés", "vadgesztenye", "dió", "mogyoró", "őszibarack",
    "körte", "alma", "szüreti bál", "színes lombok", "szeles idő",
    "takaró", "mécses", "teázás", "szüretelő fesztivál", "meleg sál"
]

paros = []

for i in range(0, len(oszi_szavak), 2):
    paros.append(oszi_szavak[i])

print(",".join(paros))


"""
3. Feladat
Készíts egy programot, ahol csak azok a számok kerülnek a listába, amik oszthatóak 3-al.
És addig kell a listához adni, ameddig a felhasználó szeretne újabb számot megadni, de legalább 5db-ot.
Ki kell írni a list hosszat és melyik a legkisebb szám a listában.
"""

print('3. Feladat')

oszthato = []

while len(oszthato) < 5: 
    szam = int(input("Kérek egy számot: "))
    if szam % 3 == 0:
        oszthato.append(szam)

    if len(oszthato) >= 5:
        break

    valasz = input("Szeretnél még számot megadni? (I/N): ").upper()
    if valasz != "I":
        break 

if len(oszthato) >= 5:
    print(f"A lista hossza: {len(oszthato)}")
    print(f"A legkisebb szám a listában: {min(oszthato)}")
else:
    print("Nem adtál meg elegendő számot, ami osztható 3-mal.")






