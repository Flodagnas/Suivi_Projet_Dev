# -*- coding: utf-8 -*-
import sqlite3

try:
    conn = sqlite3.connect('BDD.db')
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    print("Base de données crée et correctement connectée à SQLite")

    sql = "SELECT sqlite_version();"
    test = "SELECT * FROM Message;"
    cur.execute(sql)
    cur2.execute(test)
    cur3.execute("INSERT INTO \"Message\" (\"message\", \"date\", \"Pseudo\") VALUES('Test', '26/04/2022', 'Bidoof');")
    conn.commit()
    res = cur.fetchall()
    res2 = cur2.fetchall()
    print("La version de SQLite est: ", res)
    print("Le contenu de la table User est: ", res2)
    cur.close()
    cur2.close()
    cur3.close()
    conn.close()
    print("La connexion SQLite est fermée")

except sqlite3.Error as error:
    print("Erreur lors de la connexion à SQLite", error)
