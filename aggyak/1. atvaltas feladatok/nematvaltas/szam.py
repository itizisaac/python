# A. Generálj egy véletlen egész számot az [1, 50] zárt intervallumban!
# B. A program írja ki a következők egyikét
# Amennyiben a szám 5-tel osztható:
# “A szám öttel osztható!”,
# Amennyiben a szám 3-mal osztható:
# “A szám hárommal osztható!”,
# Amennyiben a szám 5-tel és 3 – mal is osztható:
# “A szám öttel és hárommal is osztható!”


import random

szam = random.randint(1,51)
print(f"A generált szám: {szam}")
if szam %5 == 0:
    print("A szám öttel osztható!")
elif szam % 3 == 0:
    print("A szám hárommal osztható!")
elif szam % 5 == 0 and szam % 3 == 0:
    print("A szám öttel és hárommal is osztható!")