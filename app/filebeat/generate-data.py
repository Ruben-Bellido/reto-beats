import json
from datetime import datetime


# Datos dummy para los archivos JSON
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data0 = {"id": 0, "state": "ON", "timestamp": timestamp}
data1 = {"id": 1, "state": "OFF", "timestamp": timestamp}

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data2 = {"id": 2, "state": "OFF", "timestamp": timestamp}
data3 = {"id": 3, "state": "ON", "timestamp": timestamp}

# Escribir los datos en los archivos JSON
with open('/usr/share/filebeat/logs/dummy_0.json', 'w') as f:
    f.write(json.dumps(data0) + '\n')
    f.write(json.dumps(data1) + '\n')

with open('/usr/share/filebeat/logs/dummy_1.json', 'w') as f:
    f.write(json.dumps(data2) + '\n')
    f.write(json.dumps(data3) + '\n')
