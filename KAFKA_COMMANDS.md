# <img src="img/udemy-logo.png" alt="udemy" width="30" style="vertical-align: middle;"> <img src="img/kafka-white-logo.png" alt="kafka" width="30" style="vertical-align: middle;"> | Apache Kafka Series - Learn Apache Kafka for Beginners  #

by [Stéphane Maarek](https://www.linkedin.com/in/stephanemaarek/) @ [ûdemy](https://www.udemy.com/course/apache-kafka/)

## Kafka commands ##

Useful kafka commands to manage kafka topics for this tutorial

____________________
### Kafka Topic 

#### Kafka Topic - Creation

##### basic syntax

**kafka-topics.sh** --bootstrap-server ***[any_broker:port]*** --topic ***[topic_name]*** --create --partitions ***[number_of_partitions]*** --replication-factor ***[number_of_partition_replicas]***

##### example for this course

```bash
kafka-topics.sh --bootstrap-server localhost:19092 --topic demo_python --create --partitions 3 --replication-factor 2
```

____________________
### Kafka Console Consumer

#### basic usage syntax

**kafka-console-consumer.sh** --bootstrap-server ***[any_broker:port]*** --topic ***[topic_name]***

#### example for this course
```bash
kafka-console-consumer.sh --bootstrap-server localhost:19092 --topic demo_python
```