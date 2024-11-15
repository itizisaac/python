lista = []

legtobb = 0
osztalyl = None

with open("menza.txt", "r", encoding="UTF8") as file:
    sorok = file.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")
        
        osztaly = sor[0]
        tanszam = int(sor[1])
        honap = sor[2]
        ar = int(sor[3])
        kedvezmeny = int(sor[4])
        lista.append([osztaly, tanszam, honap, ar, kedvezmeny])

for item in lista:
    #print(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}")
    teljesfizetes = (item[1]-item[4])*item[3]
    kedvezmenysek =  (item[3]-(item[3]*0.3))*item[4]
    print(f"{item[0]}, {round(teljesfizetes+kedvezmenysek)} Ft")
    if teljesfizetes + kedvezmenysek > legtobb:
        legtobb = teljesfizetes+kedvezmenysek
        osztalyl = item[0]
print(f"A legtöbbet fizető osztály: {osztaly}, {round(legtobb)} FT")