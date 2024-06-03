from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/solicitud', methods=['POST'])
def solicitud():
    data = request.json
    data['estado'] = 'recibido'
    producer.send('solicitudes', data)
    return jsonify({"status": "Solicitud recibida", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)