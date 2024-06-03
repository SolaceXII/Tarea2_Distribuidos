
while ! nc -z kafka 9092; do   
  echo "Esperando a que Kafka inicie..."
  sleep 1 
done

exec "$@"