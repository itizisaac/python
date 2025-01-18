# A. Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120]
# B. A bekért értékeket tárolja lista adatszerkezetben!
# C. Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)!
# D. Írj függvényt elso_idos néven, ami megkeresi az első 70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista!
# E. Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg!
# F. Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! 




def szamBekeres():
    lista = []

    while len(lista)!=5:
        szam = int(input("Adjon meg egy számot(0,120) között: "))
        lista.append(szam)
    print(":".join(map(str,lista)))
    return lista

def elso_idos(lista):
    for i in lista:
        if i > 70:
            index = lista.index(i)    
            return index

def konzolra_ir(index):
    print(f"Első idős ember korának helye a listában: {index}.")

def fajl_ir(index):
    
    with open("oreg.txt", "w", encoding="UTF8") as fajl:
        fajl.write(f"Első idős ember korának helye a listában: {index}.")

korokLista = szamBekeres()
elso = elso_idos(korokLista)
konzol = konzolra_ir(elso)
fajli = fajl_ir(elso)