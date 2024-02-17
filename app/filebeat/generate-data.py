import json

# Datos dummy para los archivos JSON
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Escribir los datos en los archivos JSON
with open('/usr/share/filebeat/data/dummy.json', 'w') as f:
    json.dump(data, f)
