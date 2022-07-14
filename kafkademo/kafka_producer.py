from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"], value_serializer=lambda x: dumps(x).encode("utf-8")
)

for i in range(20):
    data = {
        "number": i,
        "some field": "some value",
    }
    future = producer.send("demotopic", value=data)

    # To avoid race condition with producer.send() call do future.get() following send(),
    # so that we don't need to sleep(1) for every send(), else sleep(1) to be used.
    try:
        record_metadata = future.get(timeout=10)
        print("meta:", record_metadata)
    except:
        # Decide what to do if produce request failed...
        print("error in sending the message")
        pass
