import mysql

import os
import tasks


def getAllTasksQuery(uzytkownik):
    my_database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = my_database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    database_cursor.execute(f"SELECT * FROM lista_zadan where user_id='{uzytkownik}'")
    result = database_cursor.fetchall()
    return result


def selectUserQuery(uzytkownik):
    my_database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = my_database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    database_cursor.execute(f"SELECT * FROM uzytkownicy WHERE NAZWA='{uzytkownik.nazwa}'")
    result = database_cursor.fetchall()
    return result


def addTaskQuery(zadanie, uzytkownik):
    my_database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = my_database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    database_cursor.execute(
        f"INSERT INTO lista_zadan (idlista_zadan, przedmiot, nazwa_zadania, oddanie_data, skonczone,przeslane,"
        f"user_id) VALUES ('{zadanie.id}','{zadanie.przedmiot}','{zadanie.nazwa_zadania}','{zadanie.oddanie_data}',"
        f"'0','0','{uzytkownik}')")
    my_database.commit()


def removeTaskQuery(id_zadania, uzytkownik):
    database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    print(f"DELETE FROM lista_zadan WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database_cursor.execute(f"DELETE FROM lista_zadan WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database.commit()


def registerQuery(uzytkownik, haslo, salt):
    database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    haslo = haslo.decode('utf-8')
    salt = salt.decode('utf-8')
    print(f"INSERT INTO uzytkownicy(nazwa, haslo, salt) VALUES ('{uzytkownik}','{haslo}','{salt}')")
    database_cursor.execute(f"INSERT INTO uzytkownicy(nazwa, haslo, salt) VALUES ('{uzytkownik}','{haslo}','{salt}')")
    database.commit()


def finishTaskQuery(id_zadania, uzytkownik):
    database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    print(f"UPDATE lista_zadan SET skonczone=1 WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database_cursor.execute(f"UPDATE lista_zadan SET skonczone=1 WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database.commit()

def sendTaskQuery(id_zadania, uzytkownik):
    database = mysql.connector.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    database_cursor = database.cursor()
    database_cursor.execute(f"use {os.environ.get('DB_USER')}")
    print(f"UPDATE lista_zadan SET przeslane=1 WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database_cursor.execute(f"UPDATE lista_zadan SET przeslane=1 WHERE idlista_zadan={id_zadania} AND user_id='{uzytkownik}'")
    database.commit()
