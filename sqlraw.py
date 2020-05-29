import sqlite3

con = sqlite3.connect('bazadanych.db') # assigning to "con" value connection to "bazadanych.db" database
con.row_factory = sqlite3.Row # access to to records of database by indexs and NAMES
cur = con.cursor() # creating and assigning "cursor" methods to "cur" value

cur.executescript("""
DROP TABLE IF EXISTS klasa;
CREATE TABLE IF NOT EXISTS klasa (
    id INTEGER PRIMARY KEY ASC,
    nazwa varchar(250) NOT NULL,
    profil varchar(250) DEFAULT "");
""")  # methods "executescripts" is used to execute SQL instructions. "DROP TABLE" instructions deletes table "klasa".
#  "ASC" instruction - places "id" values from the smallest to the biggest one.

cur.executescript("""
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id varchar(250) NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id));
""")

cur.executemany(""" INSERT INTO klasa (id, nazwa, profil)VALUES (NULL, ?, ?);""", (("1A", "MATEMATYCZNY"),
                                                                                   ("1B", "HUMANISTYCZNY")))

cur.execute(""" SELECT id FROM klasa WHERE nazwa = ? """, ("1A",))
klasa_id = cur.fetchone()[0]

uczniowie = (
    (None, "Tomasz", "Ficek", klasa_id),
    (None, "Paulina", "Spyrka", klasa_id),
    (None, "Jan", "Kowalski", klasa_id)
)  #  creating "tuple" objects uczniowie

cur.executemany(""" INSERT INTO uczen(id, imie, nazwisko, klasa_id) VALUES(?, ?, ?, ?)""", (uczniowie))
con.commit()  # methods "commit" confirm/save in database above operation

def czytaj_dane():
    cur.execute(""" SELECT uczen.id, imie, nazwisko,nazwa, profil FROM klasa, uczen
     WHERE uczen.klasa_id = klasa.id """)
    uczniowie = cur.fetchall() # "fetchall" methods fetches(extracts/bring) all rows from table as a "tuple" list object
    for uczen in uczniowie:
        print(uczen["id"], uczen["imie"], uczen["nazwisko"], uczen["nazwa"], "klasa o profilu", uczen["profil"])

czytaj_dane()

cur.execute(""" SELECT id FROM klasa WHERE nazwa = ?""", ("1B",))
klasa_id = cur.fetchone()[0]
cur.execute(""" UPDATE uczen SET klasa_id = ? WHERE id = ? """, (klasa_id, 2))
czytaj_dane()
cur.close()

