mennyi = int(input("Írd be mennyi pénzed van: "))

while mennyi > 0:
    kolt = int(input("Írd be mennyit szeretnél költeni belőle: "))

    if kolt > mennyi:
        print("Ennyit nem költhetsz, nincs elég pénzed!.")
    else:
        mennyi -= kolt
        print(f"Ennyi pénzed maradt: {mennyi}")
