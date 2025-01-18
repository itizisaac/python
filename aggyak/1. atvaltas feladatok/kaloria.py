tabor_neve = input("Adja meg a tábor nevét: ")

kaloriak = []

print("Adja meg az egyes napok elégetett kalóriáit!")

print("Legalább 5 nap adatait meg kell adnia.")

for i in range(5):
    kaloria = int(input(f"Adjon meg egy napi kalóriaértéket (jelenlegi adatok száma: {i}): "))
    kaloriak.append(kaloria)

while True:
    valasz = input("Szeretne további kalóriákat hozzáadni? (i/n): ").lower()
    if valasz == "n":
        break
    elif valasz == "i":
        kaloria = int(input(f"Adjon meg egy napi kalóriaértéket (jelenlegi adatok száma: {len(kaloriak)}): "))
        kaloriak.append(kaloria)
    else:
        print("Érvénytelen válasz, kérlek válaszolj 'i' vagy 'n'.")

atlag = sum(kaloriak) / len(kaloriak)

print("===== Heti Kalóriaösszegzés =====")
print(f"Tábor neve: {tabor_neve}")
print(f"Átlagosan elégetett kalória naponta: {int(atlag)} kcal")
