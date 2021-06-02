import mysql.connector
import json

def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="",
                                  database="db_ble_sentral")
    return sql

def input_data(type_ble,uuid,major,minor,rss,mac_adress,ruangan):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO `tb_data`(`type`, `uuid`, `major`, `minor`, `rssi`, `mac_address`, `ruangan`) VALUES (%s,%s,%s,%s,%s,%s,%s)",(type_ble,uuid,major,minor,rss,mac_adress,ruangan))
        db.commit()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)

