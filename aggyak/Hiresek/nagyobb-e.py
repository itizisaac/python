# Írjon programot nagyobb.py néven! A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb! A program üzeneteinek megfogalmazásában kövesse az alábbi példát! Azokat a részeket, amiket a felhasználó gépel be, a mintában vastagított és döntött betűkkel emeltük ki.

szam1 = int(input("Adj meg egy számot!"))
szam2 = int(input("Adj meg egy másik számot!"))

if szam1 > szam2:
   print(f"A nagyobb érték {szam1}")
elif szam2 > szam1:
    print(f"A nagyobb érték {szam2}")
else:
    print(f"A két szám egyenlő")