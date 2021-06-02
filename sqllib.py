from os import curdir
import mysql.connector
import json


def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="",
                                  database="db_ble")
    return sql
 

def input_data(type_ble,uuid,major,minor,rss,mac_adress):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO `tb_data`(`type`, `uuid`, `major`, `minor`, `rssi`, `mac_address`) VALUES (%s,%s,%s,%s,%s,%s)",(type_ble,uuid,major,minor,rss,mac_adress))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)


def ambil_data():
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `type`, `uuid`, `major`, `minor`, `rssi`, `mac_address` FROM `tb_data`")
        rows = [x for x in cursor]
        cols = [x[0] for x in cursor.description]
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        rows = []
        cols = []
    datas = []
    for row in rows:
        data = {}
        for prop, val in zip(cols, row):
            data[prop] = val
        datas.append(data)
    return datas



     