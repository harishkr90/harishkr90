## Kafka commands

#### Start Zookeeper
./bin/zookeeper-server-start.sh config/zookeeper.properties 
#### Start kafka server
./bin/kafka-server-start.sh config/server.properties

#### Create Topic
./bin/kafka-topics.sh --create --topic demotopic --bootstrap-server localhost:9092
#### List all topics 
./bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
#### Delete topic
./bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic demotopic

### more information here:
https://www.conduktor.io/kafka/kafka-topics-cli-tutorial
https://kafka.apache.org/quickstart


## Python packages required

pip3 install kafka-python
