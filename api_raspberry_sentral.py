from flask import request,Flask,jsonify
from sqlib_sentral import input_data,cek_data_ble,update_table_data

app = Flask(__name__)

@app.route('/r1/input',methods=['POST'])
def data_input():
    json_data = request.json
    if json_data==None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'type_ble' not in json_data or 'uuid' not in json_data or 'minor' not in json_data or 'major' not in json_data or 'rssi' not in json_data or 'mac_address' not in json_data or 'ruangan' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            type_ble = json_data['type_ble']
            uuid = json_data['uuid']
            minor = json_data['minor']
            major = json_data['major']
            rssi = json_data['rssi']
            mac_address = json_data['mac_address']
            ruangan = json_data['ruangan']
            cek = cek_data_ble(uuid)
            if cek==False:
                update_table_data(type_ble,major,minor,rssi,mac_address,ruangan,uuid)
                result = {"message": "Update success"}
                resp = jsonify(result)
                return resp, 200
            else:
                input_data(type_ble,uuid,major,minor,rssi,mac_address,ruangan)
                result = {"message": "Input success"}
                resp = jsonify(result)
                return resp, 202
            
if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=6000)
    app.run(port=6000, debug=True)