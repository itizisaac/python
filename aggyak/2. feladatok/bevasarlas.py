arak = []

uzlet = input("Adja meg az üzlet nevét: ")

while True:
    ar = int(input("Adja meg termék árát: "))
    arak.append(ar)

    if len(arak) == 4:
        szeretne = input("Szeretne még egy termék árát megadni? (igen/nem): ")
        if szeretne != "igen":
            break

print(f"Üzlet neve: {uzlet}")
print(f"Átlagos költség: {round(sum(arak) / len(arak))} Ft")