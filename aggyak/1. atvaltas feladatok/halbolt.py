print("Üdvözöljük a halboltban! \n Kétféle hal kapható: \n Lazac - 3000 Ft/kg \nPisztráng - 2500 Ft/kg")

hal = input("Kérem, válassza ki a halat (lazac/pisztráng): ")
kg = int(input("Kérem, adja meg, hány kilogrammot szeretne vásárolni: "))

if hal == "lazac" or "pisztráng":
    print(f"A választott hal: {hal}")
    print(f"Mennyiség: {kg} kg")
else:
    print("Nincs ilyen hal.")

if hal == "lazac":
    print(f"Az összeg: {3000 * kg} Ft")
elif hal == "pisztáng":
    print(f"Az összeg: {2500 *kg} Ft")