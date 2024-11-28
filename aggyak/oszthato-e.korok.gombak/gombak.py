# A. Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza!
# B. Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama!
# C. Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában? A metódus neve legyen papsapka!
# D. Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen

def beolvas(fajlkezeles):
    lista = []
    with open(fajlkezeles, "r", encoding="UTF8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split("@")

            gomba_nev = sor[0]
            nemzetseg =sor[1]
            evszak = sor[2]

            lista.append([gomba_nev, nemzetseg,evszak])
        # for item in lista:
        #     print(f"{item[0]}, {item[1]}, {item[2]}")
    return lista
def gombak_szama(lista):
    print(f"A gombák száma: {len(lista)}")


def papsapka(lista):
    for item in lista:
        if item[1] == "papsapkagombák ":
           nev = item[0]           
           return nev
            
def kiir(nev):
    print(nev)
    

beolv = beolvas("gombak.txt")
szam = gombak_szama(beolv)
p = papsapka(beolv)
k = kiir(p)
