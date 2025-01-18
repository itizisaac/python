def beolvasas(fajkezeles):
    lista = []
    with open(fajkezeles, "r", encoding="utf8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split("#")

            szelesseg = int(sor[0])
            magassag = int(sor[1])
            melyseg = int(sor[2])
            suly = int(sor[3])
            lista.append([szelesseg, magassag, melyseg, suly])

        for item in lista:
            print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")
    
    return lista

def pogyasz_szam(lista):
    print(f"A pogyászok száma: {len(lista)}")

def atlag_suly(lista):
    sulyok = [item[3] for item in lista if item[0] == 51]
    if sulyok:
        print(f"Az 51 cm-es poggyászok átlag súlyértéke: {round(sum(sulyok) / len(sulyok) * 1000)} g.")
    else:
        print("Nincs 51 cm-es poggyász.")

def legmagasabb(lista):
    legmagagasabb = lista[0][1]
    legszelesebb = lista[0][0]
    legmelyebb = lista[0][2]
    legnagyobb = lista[0][3]

    for item in lista:
        if item[1] > legmagagasabb:
            legmagagasabb = item[1]
            legszelesebb = item[0]
            legmelyebb = item[2]
            legnagyobb = item[3]
    
    print(f"A legmagasabb poggyász méretei: {legszelesebb}x{legmagagasabb}x{legmelyebb} súly: {legnagyobb}")

beolv = beolvasas("csomag.txt")
pogyasz_szam(beolv)
atlag_suly(beolv)
legmagasabb(beolv)
