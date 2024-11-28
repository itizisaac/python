# Az elkészítendő program bekéri három híres nő nevét, foglalkozását, illetve nemzetiségét, amely angol vagy német lehet. Ezt a három adatot minden esetben egy-egy objektumban tárolja. Az adatok megadását követően a program a mintának megfelelően, a nemzetiségtől függően Ms. (angolok) vagy Frau (németek) előtaggal együtt kiírja az objektumokban tárolt neveket és foglalkozásokat. Az adatokat egy hiresnok.txt fájlba kell kiírni.

lista=[]

for i in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    fogalkozas = input("Add meg a foglalkozását!")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)!")
    lista.append([nev,fogalkozas,nemzetiseg])

with open("hiresnok.txt", "w", encoding="UTF8") as fajl:

    for list in lista:
        if list[2] == "a":
            fajl.write(f"Ms.{list[0]}egy híres {list[1]}")
        else:
            fajl.write(f"Frau {list[0]}egy híres {list[1]}")