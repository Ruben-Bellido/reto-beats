# reto-beats

• Pasos seguidos:
- Planteamiento y creación de la estructura del proyecto
- Desarrollo del programa de generación de archivos de logs dummy
- Investigación acerca de docker compose
- Investigación acerca de elasticsearch y filebeat y su implementación en docker/docker compose
- Desarrollo del docker compose
- Desarrollo de la configuración de filebeats para recibir los datos dummy e ingerirlos a elasticsearch
- Comprobación del correcto funcionamiento vía Postman

• Instrucciones de uso:
- Extraer contenido del .zip
- Estando en el directorio app, ejecutar $ docker-compose up -d
- Para comprobar que se haya ejecutado correctamente, hacer una llamada GET a la dirección http://localhost:9200/dummy vía Postman

• Posibles vías de mejora:
- Generar diferentes índices que almacenen datos dummy
- Generar datos dummy aleatorios de manera constante

• Problemas / Retos encontrados:
- Configuración de puertos y seguridad de elasticsearch, no era posible acceder a los índices sin las configuraciones correctas
- Transferencia de datos dummy de filebeats a elasticsearch, no se realizaba correctamente y no quedaba claro el motivo de fallo

• Alternativas posibles:
- Tecnologías similares alternativas de otras compañías
