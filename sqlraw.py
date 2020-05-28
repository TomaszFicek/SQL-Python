import sqlite3

con = sqlite3.connect('bazadanych.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS klasa;
CREATE TABLE IF NOT EXISTS klasa (
    id INTEGER PRIMARY KEY ASC,
    nazwa varchar(250) NOT NULL,
    profil varchar(250) DEFAULT "");
""")

cur.executescript("""
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id varchar(250) NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id));
""")