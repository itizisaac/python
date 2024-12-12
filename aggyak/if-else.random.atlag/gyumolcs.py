print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümölcs kapható:")
print("1. Alma - 150 Ft/db")
print("2. Körte - 200 Ft/db")

gyumolcs = input("Kérem, válassza ki a gyümölcsöt (alma/körte): ").lower()
mennyiseg = int(input("Kérem, adja meg, hány darabot szeretne vásárolni: "))

ar_alma = 150
ar_korte = 200

if gyumolcs == "alma":
    fizetes = ar_alma * mennyiseg
    print(f"A választott gyümölcs: Alma")
    print(f"Mennyiség: {mennyiseg} darab")
    print(f"Fizetendő összeg: {fizetes} Ft")
elif gyumolcs == "körte":
    fizetes = ar_korte * mennyiseg
    print(f"A választott gyümölcs: Körte")
    print(f"Mennyiség: {mennyiseg} darab")
    print(f"Fizetendő összeg: {fizetes} Ft")
else:
    print("Érvénytelen gyümölcs választás. Kérem, válasszon alma vagy körte közül.")