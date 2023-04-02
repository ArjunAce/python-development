from kafka import KafkaConsumer

consumer = KafkaConsumer('hello-world-topic', bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message.value.decode())
