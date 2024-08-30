<img src="https://github.com/user-attachments/assets/f2d90a13-94e3-4c9b-91e3-8b74d8b0e85f" alt="Image description" width="900" />


## Setting Up a Multi-Node Spark Cluster Locally Using Docker and Docker Compose

This guide will walk you through setting up a multi-node Apache Spark cluster locally using Docker and Docker Compose. Follow the steps below to get started.

### Prerequisites
Before starting, make sure you have the following software installed on your system:

Docker Desktop: Docker allows you to containerize applications. If you don’t have Docker Desktop installed, you can download and install it from the official Docker documentation:
https://docs.docker.com/engine/install/

Docker Compose: Docker Compose is a tool for defining and running multi-container Docker applications. You can install Docker Compose following the instructions here:
https://docs.docker.com/compose/install/

Note that Docker Desktop includes Docker Compose by default, so you might not need to install it separately if you have Docker Desktop.

Python 3: Python is required for running certain scripts. Download and install Python 3 from the official Python website:
https://www.python.org/downloads/

Git: Git is needed for cloning repositories. Install Git from the official Git website:
https://git-scm.com/downloads/

### Setup instructions:

* First, clone the repository that contains the Docker configuration for the Spark cluster::
  ```
  https://github.com/Rishav273/spark-cluster-multi-node-setup.git
  ```
  
* Change your working directory to the folder where the repository was cloned:
  ```
  cd spark-cluster-multi-node-setup
  ```
  

* Install the necessary Python dependencies listed in the requirements.txt file::
  ```
  pip install -r requirements.txt
  ```
  
  
* Use Docker Compose to bring up the Spark cluster in detached mode. This will start all the containers defined in the docker-compose.yml file::
  ```
  docker-compose up -d
  ```
  The -d flag runs the containers in detached mode, meaning they will run in the background.
  

* After starting the containers, verify that the Spark cluster is up and running by opening the Spark Web UI in your browser::
  ```  
  http://localhost:8080/
  ```
  You should see the Spark master web interface, indicating that your multi-node Spark cluster is running correctly.

### Conclusion
You have successfully set up a multi-node Spark cluster locally using Docker and Docker Compose. You can now use this environment for distributed data processing with Apache Spark.
