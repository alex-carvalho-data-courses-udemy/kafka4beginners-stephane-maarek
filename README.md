# <img src="img/udemy-logo.png" alt="udemy" width="30" style="vertical-align: middle;"> <img src="img/kafka-white-logo.png" alt="kafka" width="30" style="vertical-align: middle;"> | Apache Kafka Series - Learn Apache Kafka for Beginners  #

by [Stéphane Maarek](https://www.linkedin.com/in/stephanemaarek/) @ [ûdemy](https://www.udemy.com/course/apache-kafka/)

## What is this repository for? ##

### Quick summary

Repository to follow the course [Apache Kafka Series - Learn Apache Kafka for Beginners](https://www.udemy.com/course/apache-kafka/)

### Course Info

<img src="img/kafka-white-logo.png" alt="kafka" width="100">

[Apache Kafka Series - Learn Apache Kafka for Beginners](https://www.udemy.com/course/apache-kafka/) 
on [udemy](https://www.udemy.com) 
by [Stephane Maarek](https://www.linkedin.com/in/stephanemaarek/)  

09-2022 (taken)

#### Course materials

The original course code material provided by Stephane are placed at:  

```bash
course-materials/
```


## How do I get set up? ##

### Summary of set up

1. Orchestrated (terraform)
1.1. Initialize Terraform
1.1. Build terraform infrastructure 

2. Manual (docker)
2.1. Create docker images  
2.1.1. ***kafka-base*** image  
2.1.2. ***kafka-zookeper*** image  
2.1.3. ***kafka-server*** image  
2.2. Create Docker Network
2.3. Start Docker containers
2.3.1. ***kafka-zookeeper*** container
2.3.2. ***kafka-server*** container

### Dependencies

- docker version >=20.10.17  
- terraform >=1.2.8  
- kafka 2.13-3.2.1  

### Configuration

#### 1. Orchestrated (terraform)

##### 1.1. Initialize Terraform

go to terraform build folder
```bash
cd infra/terraform/build/
```

##### 1.1. Build terraform infrastructure 

#### 2. Manual (docker)

##### 2.1. Create docker images  

###### 2.1.1. **kafka-base**  

build ***kafka-base*** docker image

```bash
docker build --file infra/docker/images/kafka-base/Dockerfile --tag kafka-base:latest --tag kafka-base:3.2.1-1.0.0 .
```

###### 2.1.2. **kafka-zookeepr**  

```bash
docker build --file infra/docker/images/kafka-zookeeper/Dockerfile --tag kafka-zookeper:latest --tag kafka-zookeper:3.2.1-1.0.0 .
```

###### 2.1.3. **kafka-server**  

```bash
docker build --file infra/docker/images/kafka-server/Dockerfile --tag kafka-server:latest --tag kafka-server:3.2.1-1.0.0 .
```

##### 2.2. Create Docker Network

```bash
docker network create kafka-network
```

##### 2.3. Start Docker containers

###### 2.3.1. ***kafka-zookeeper*** container

```bash
docker container run -d --rm --name kafka-zookeeper --network kafka-network kafka-zookeeper:latest
```

###### 2.3.2. ***kafka-server*** container

```bash
docker container run -d --rm --network kafka-network --publish 9092:9092 kafka-server:latest zookeeper.connect=kafka-zookeeper:2181
```

### How to run tests

#### 1. Check terraform build

##### 1.1. Validate terraform build files

go to terraform build folder

```bash
cd infra/terraform/build/
```

validate the files

```bash
terraform validate
```

##### 1.2. Check terraform build state

go to terraform build folder

```bash
cd infra/terraform/build/
```

check the resources state

```bash
terraform state list
```

#### 2. Check terraform exec

##### 2.1. Validate terraform exec files

go to terraform exec folder

```bash
cd infra/terraform/exec/
```

validate the files

```bash
terraform validate
```

##### 2.2. Check terraform exec state

go to terraform exec folder

```bash
cd infra/terraform/exec/
```

check the resources state

```bash
terraform state list
```

### Deployment instructions

go to terraform exec folder

```bash
cd infra/terraform/exec/
```

apply terraform infrastructure

```bash
terraform apply
```

## Kafka cli commands ##

[kafka cli commands](KAFKA_COMMANDS.md) used in this tutorial.  

## Who do I talk to? ##

### Repo owner or admin

[alex carvalho](alex.carvalho.data@gmail.com)
