from sqllib import ambil_data
import requests

url = "http://ipraspberry:port/path" # sesuai rasberry
data =  ambil_data()

for i in range(0,len(data)):
    data[i]['ruangan'] = 1 # bisa ganti sesuai rasberry di ruang berapa

for i in range(0,len(data)):
    x =  requests.post(url=url,data=data[i])
    print(x.text)




