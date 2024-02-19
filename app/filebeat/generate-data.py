import json
import random
import time
from datetime import datetime

# Inicializar id
id = 0

# Bucle indefinido
while True:
  # Datos dummy para los archivos JSON
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  data0 = {"data":{"id": id, "state": random.randint(0, 1), "timestamp": timestamp}}
  data1 = {"data":{"id": id, "state": random.randint(0, 1), "timestamp": timestamp}}

  # Escribir los datos en los archivos JSON
  with open('/usr/share/filebeat/logs/dummy_0.json', 'a') as f:
      f.write(json.dumps(data0) + '\n')

  with open('/usr/share/filebeat/logs/dummy_1.json', 'a') as f:
      f.write(json.dumps(data1) + '\n')

  # Incrementar id
  id += 1
  
  # Esperar 10s
  time.sleep(10)
