import hashlib
import hmac
import os

import bcrypt
import pymysql
import classes


def databaseConnector():
    my_database = pymysql.connect(
        host=os.environ.get("DB_HOSTNAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return my_database


def establishConnection():
    database_cursor = databaseConnector().cursor()
    return database_cursor


def prepareList(myresult):
    lista_zadan = []
    result = ""
    for x in myresult:
        lista_zadan.append(
            classes.Zadanie(id=x[0], przedmiot=x[1], nazwa_zadania=x[2], oddanie_data=x[3], skonczone=int(x[4]),
                            przeslane=int(x[5])))
    lista_zadan.sort(key=lambda poj_zadanie: poj_zadanie.id)
    if len(lista_zadan)>0:
        najw_index = lista_zadan[-1].id
    else:
        najw_index = 0
    lista_zadan.sort(key=lambda poj_zadanie: poj_zadanie.ile_dni)
    for zadanie in lista_zadan:
        result += zadanie.sendStatement()
    return result, najw_index

#TODO: REFACTOR
# SALT MUST BEADDED TO PASSWORD BEFORE HASHING


def loginTry(uzytkownik, stored_password, stored_salt):
    stored_salt=stored_salt.encode()
    password = uzytkownik.haslo
    password = password.encode() + stored_salt
    hashed = hashlib.sha256(password)
    hashed = hashed.hexdigest()
    print(f"{password}, {stored_password}, {hashed}, {stored_salt.decode()}")
    return stored_password == hashed


def hashPassword(haslo):
    hashed_password= hashlib.sha256(haslo.encode())
    return hashed_password
