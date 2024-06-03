from kafka import KafkaConsumer, KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
consumer = KafkaConsumer('solicitudes', bootstrap_servers='kafka:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

estado_secuencia = {
    'recibido': 'preparando',
    'preparando': 'entregando',
    'entregando': 'finalizado'
}

def procesar_solicitud(data):
    estado_actual = data['estado']
    if estado_actual in estado_secuencia:
        time.sleep(5) 
        data['estado'] = estado_secuencia[estado_actual]
        print(f"Cambiando estado a: {data['estado']}")
        producer.send('solicitudes', data)

for message in consumer:
    solicitud = message.value
    print(f"Mensaje recibido: {solicitud}") 
