import random

jatekok = []

while True:
    kedvenc = input("Add meg 4 kedvenc videójátékodat!")
    jatekok.append(kedvenc)
    if len(jatekok) == 4:
        break

print(f"1. Játék: {kedvenc}")
print(f"2. Játék: {kedvenc}")
print(f"3. Játék: {kedvenc}")
print(f"4. Játék: {kedvenc}")

kedvencjatekok = ", ".join(jatekok)

print(f"A kedvenc videójátékaid: {kedvencjatekok}")

evjateka = random.choice(jatekok)

print(f"A 2025 év játéka: {evjateka}")