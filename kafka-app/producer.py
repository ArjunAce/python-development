from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

message = "Hello, Kafka!"

producer.send('hello-world-topic', message.encode())
producer.flush()


