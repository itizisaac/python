import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS konyvtar")
conn.database = "konyvtar"


cursor.execute("""
CREATE TABLE IF NOT EXISTS konyvek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cim VARCHAR(255) NOT NULL,
    szerzo VARCHAR(255) NOT NULL,
    ev INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS olvasok (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nev VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS kolcsonzesek (
    id INT AUTO_INCREMENT PRIMARY KEY,
    konyv_id INT,
    olvaso_id INT,
    kolcsonzes_datum DATE,
    visszahozas_datum DATE,
    FOREIGN KEY (konyv_id) REFERENCES konyvek(id),
    FOREIGN KEY (olvaso_id) REFERENCES olvasok(id)
)
""")

konyvek = [
    ("Egri csillagok", "Gárdonyi Géza", 1899),
    ("A Pál utcai fiúk", "Molnár Ferenc", 1907),
    ("Tüskevár", "Fekete István", 1957),
    ("Légy jó mindhalálig", "Móricz Zsigmond", 1920),
    ("Az arany ember", "Jókai Mór", 1872),
    ("A kőszívű ember fiai", "Jókai Mór", 1869),
    ("Ida regénye", "Gárdonyi Géza", 1904),
    ("Abigél", "Szabó Magda", 1970),
    ("A Noszty fiú esete Tóth Marival", "Mikszáth Kálmán", 1908),
    ("Szent Péter esernyője", "Mikszáth Kálmán", 1895)
]
cursor.executemany("INSERT INTO konyvek (cim, szerzo, ev) VALUES (%s, %s, %s)", konyvek)

olvasok = [
    ("Kovács Anna", "anna.kovacs@example.com"),
    ("Nagy Péter", "peter.nagy@example.com"),
    ("Szabó László", "laszlo.szabo@example.com"),
    ("Tóth Júlia", "julia.toth@example.com"),
    ("Farkas Dániel", "daniel.farkas@example.com")
]
cursor.executemany("INSERT INTO olvasok (nev, email) VALUES (%s, %s)", olvasok)

conn.commit()

cursor.execute("SELECT id FROM konyvek")
konyv_idk = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM olvasok")
olvaso_idk = [row[0] for row in cursor.fetchall()]

kolcsonzesek = [
    (konyv_idk[0], olvaso_idk[0], "2025-04-01", None),
    (konyv_idk[1], olvaso_idk[1], "2025-03-15", "2025-04-01"),
    (konyv_idk[2], olvaso_idk[2], "2025-03-20", None),
    (konyv_idk[3], olvaso_idk[3], "2025-03-05", "2025-03-15"),
    (konyv_idk[4], olvaso_idk[4], "2025-04-05", None),
    (konyv_idk[5], olvaso_idk[0], "2025-04-02", None),
    (konyv_idk[6], olvaso_idk[1], "2025-03-28", "2025-04-07"),
    (konyv_idk[7], olvaso_idk[2], "2025-04-08", None),
    (konyv_idk[8], olvaso_idk[3], "2025-03-30", "2025-04-05"),
    (konyv_idk[9], olvaso_idk[4], "2025-04-09", None)
]
cursor.executemany("""
INSERT INTO kolcsonzesek (konyv_id, olvaso_id, kolcsonzes_datum, visszahozas_datum)
VALUES (%s, %s, %s, %s)
""", kolcsonzesek)

conn.commit()

cursor.execute("""
SELECT olvasok.nev, konyvek.cim, kolcsonzesek.kolcsonzes_datum, kolcsonzesek.visszahozas_datum
FROM kolcsonzesek
JOIN olvasok ON kolcsonzesek.olvaso_id = olvasok.id
JOIN konyvek ON kolcsonzesek.konyv_id = konyvek.id
ORDER BY kolcsonzesek.kolcsonzes_datum DESC
""")

print("\nKölcsönzések:")
for sor in cursor.fetchall():
    print(f"{sor[0]} kölcsönözte: '{sor[1]}' | Dátum: {sor[2]} | Visszahozva: {sor[3]}")

cursor.close()
conn.close()