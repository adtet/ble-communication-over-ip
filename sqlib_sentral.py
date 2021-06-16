import mysql.connector
import json

from mysql.connector import cursor

def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="",
                                  database="db_ble_sentral")
    return sql

def input_data(type_ble,uuid,major,minor,rss,mac_adress,ruangan,status):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO `tb_data`(`type`, `uuid`, `major`, `minor`, `rssi`, `mac_address`, `ruangan`,`status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(type_ble,uuid,major,minor,rss,mac_adress,ruangan,status))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        

def cek_data_ble(uuid):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT  `uuid` FROM `tb_data` WHERE `uuid`=%s",(uuid,))
        c = cursor.fetchone()
    except(mysql.connector.Warning,mysql.connector.Error) as e:
        print(e)
        c = None
    if c==None:
        return True
    else:
        return False
    

def update_table_data(type_ble,major,minor,rssi,mac_address,ruangan,uuid,status):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE `tb_data` SET `type`=%s,`major`=%s,`minor`=%s,`rssi`=%s,`mac_address`=%s,`ruangan`=%s,`status`=%s WHERE `uuid`=%s",(type_ble,major,minor,rssi,mac_address,ruangan,status,uuid))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

def cek_room(uuid,ruangan):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `uuid`, `ruangan` FROM `tb_room` WHERE `uuid`=%s AND `ruangan`=%s",(uuid,ruangan))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        return True

def cek_room_base_uuid(uuid):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `uuid` FROM `tb_room` WHERE `uuid`=%s",(uuid,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        return True