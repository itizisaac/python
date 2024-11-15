import random

def szamok():
    lista = []
    for i in range(1, 13):
        szam = random.randint(-10,1000)
        lista.append(szam)
    print("$".join(map(str,lista)))
    return lista


def paratlan_szamok(lista):
    paratlan = 0
    for item in lista:
        if item %2 != 0:
            paratlan += 1
    return paratlan

def konzol(paratlan):
    print(f"A páratlanok száma: {paratlan}")

def fajlba(paratlan):
    with open("eredmeny.txt", "w", encoding="UTF8") as file:
        file.write(f"A páratlanok száma: {paratlan}")

sz = szamok()
par = paratlan_szamok(sz)
k = konzol(par)
f = fajlba(par)