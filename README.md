# reto-beats

Pasos seguidos:
- Investigación acerca de Docker Compose
- Investigación acerca de Elasticsearch junto al uso de su API y Filebeat y la respectiva implementación de ambos en Docker/Docker Compose
- Planteamiento y creación de la estructura del proyecto
- Desarrollo del programa de generación de archivos de logs dummy
- Desarrollo del archivo Docker encargado de crear un contenedor que contenga el programa que genera los datos dummy de manera indefinida
- Desarrollo del Docker Compose incluyendo los servicios de generación de logs dummy, Elasticsearch y Filebeats
- Desarrollo de la configuración de Filebeats para recibir los datos dummy e ingerirlos a Elasticsearch
- Comprobación del correcto funcionamiento vía Postman


Instrucciones de uso:
- Estando en el directorio app, ejecutar $ docker-compose up -d
- Para comprobar que se haya ejecutado correctamente, hacer una llamada GET a la dirección http://localhost:9200/_cat/indices?v y comprobar si se han añadido los índices y si la cantidad de documentos que estos contienen coinciden con la cantidad de datos dummy generados (tarda al rededor de 1m en estar listo)
- Comprobar los datos dummy en la propiedad data de la salida al hacer las llamadas GET a los diferentes índices http://localhost:9200/dummy0/_search y http://localhost:9200/dummy1/_search


Posibles vías de mejora:
- Posibilidad de ingerir datos de fuentes externas que no sean el pograma de generación de datos dummy
- Posibilidad de añadir el servicio de parseo de logs Logstash o el servicio de visualización y análisis de datos Kibana


Problemas / Retos encontrados:
- Comprensión de como hacer uso de Docker Compose
- Configuración de puertos y seguridad de Elasticsearch, no era posible acceder a los índices sin las configuraciones correctas
- Transferencia de datos dummy de Filebeats a Elasticsearch, no se realizaba correctamente debido a configuraciones de puertos
- Configurar Filebeat para, por ejemplo, añadir índices adicionales o parsear los datos
- Comprobación de errores en los logs durante la ejecución, resulta muy poco intuitivo al no estar resaltados


Alternativas posibles:
- Sustituir Filebeat por Logstash, este último aporta la ventaja de que puede transformar los datos antes de enviarlos
- Hacer uso de Kubernetes en lugar de Docker Compose, Kubernetes está dedicado a implementaciones más complejas y proporciona características adicionales como autoescalado y balanceo de carga
