# 1.Feladat
# Készíts egy programot amivel a megadott listából ki kell választani melyek azok a szavak,
# amelyek hosszúságának az értéke 5 és ki kell íratni a konzolra melyek ezek a szavak
# és hány darab van belőlük.

szavak = [
    "alma", "asztal", "doboz", "ceruza", "egér", "fotel",
    "szék", "pohár", "táblázat", "könyv", "kulcs", "karkötő",
    "mobiltelefon", "számítógép", "egérpad", "monitor", "hangszóró", "szék",
    "asztalterítő", "függöny", "szőnyeg", "párna", "papucs", "cipőfűző",
    "naptár", "hűtőszekrény", "mosogatógép", "főzőlap", "mikrohullámú",
    "nyomtató", "scanner", "projektor", "távirányító", "szendvics",
    "tolltartó", "jegyzetfüzet", "irattartó", "mappa", "papír",
    "töltőtoll", "hegyező", "ragasztószalag", "füzet", "kapocs",
    "toll", "filctoll", "színesceruza", "vonalzó", "radír"
]


otbetus = []

for szo in szavak:
    if len(szo) == 5:
        otbetus.append(szo)

print(f"5 betűs szavak: {', '.join(otbetus)} | Darabszám: {len(otbetus)}")


# 2.Feladat
# Kérj be születési évszámokat és számold ki a kort és azt add a listához.
# Írd ki a konzolra, hány db kor szerepel és melyik a legnagyobb kor a listában.

from datetime import datetime

evszam = False

kor = []

while not evszam:
    evek = int(input("Adj meg születési évszámokat: "))
    kor.append(datetime.now().year - evek)
    valasz = input("Szeretnél még meadni évszámokat?").upper()
    if valasz != "I":
        evszam = True
        break

print(kor)
print(f"A korok száma: {len(kor)}")
print(f"A legnagyobb kor: {max(kor)}")





