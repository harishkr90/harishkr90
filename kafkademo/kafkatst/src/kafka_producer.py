from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"], value_serializer=lambda x: dumps(x).encode("utf-8")
)

for i in range(20):
    data = {
        "number": i,
        "harish field": "some value to test so that i can check the size of the log ffile in the tmp kafka demo folder, which would reveal me the logic behind the working of kafka after each insertion. hope you get it. ZZZ!!!zzzzzzzzzzzzzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA11111111111111111111111111111111",
    }
    producer.send("demotopic", value=data)
    sleep(3)
