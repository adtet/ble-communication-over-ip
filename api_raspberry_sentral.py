from flask import request,Flask,jsonify
from sqlib_sentral import input_data,cek_data_ble,update_table_data,cek_room,cek_room_base_uuid

app = Flask(__name__)

@app.route('/r1/input',methods=['POST'])
def data_input():
    json_data = request.json
    if json_data==None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'type' not in json_data or 'uuid' not in json_data or 'minor' not in json_data or 'major' not in json_data or 'rssi' not in json_data or 'macAddress' not in json_data or 'ruangan' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            type_ble = json_data['type']
            uuid = json_data['uuid']
            minor = json_data['minor']
            major = json_data['major']
            rssi = json_data['rssi']
            mac_address = json_data['macAddress']
            ruangan = json_data['ruangan']
            cek = cek_data_ble(uuid)
            if cek==False:
                cek_ruangan = cek_room(uuid,ruangan)
                if cek_ruangan==False:
                    status = "forbidden"
                    update_table_data(type_ble,major,minor,rssi,mac_address,ruangan,uuid,status)
                    result = {"message": "Update success",
                              "status":status}
                    resp = jsonify(result)
                    return resp, 203
                else:
                    status = "allow"
                    update_table_data(type_ble,major,minor,rssi,mac_address,ruangan,uuid,status)
                    result = {"message": "Update success",
                              "status":status}
                    resp = jsonify(result)
                    return resp, 200                        
            else:
                cek_ruangan = cek_room_base_uuid(uuid)
                if cek_ruangan==False:
                    result = {"message": "Forbidden device"}
                    resp = jsonify(result)
                    return resp, 403
                else:
                    cek_ruangan_lagi = cek_room(uuid,ruangan)
                    if cek_ruangan_lagi==False:
                        status = "forbidden"
                        input_data(type_ble,uuid,major,minor,rssi,mac_address,ruangan,status)
                        result = {"message": "Input success"}
                        resp = jsonify(result)
                        return resp, 202
                    else:
                        status = "allow"
                        input_data(type_ble,uuid,major,minor,rssi,mac_address,ruangan,status)
                        result = {"message": "Input success"}
                        resp = jsonify(result)
                        return resp, 202
                        
if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=6000)
    app.run(port=6000, debug=True)