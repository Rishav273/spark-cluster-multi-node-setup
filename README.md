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
  
* Create a local virtual environment for installing all dependencies and activate it:
  ```
  python -m venv venv # windows
  venv\Scripts\activate # windows
  
  python3 -m venv venv # macOS
  source venv/bin/activate # macOS
  ```


* Install the necessary Python dependencies listed in the requirements.txt file::
  ```
  pip install -r requirements.txt
  ```
  
  
* Use Docker Compose to bring up the Spark cluster in detached mode. This will start all the containers defined in the docker-compose.yml file::
  ```
  docker-compose up --build -d  # Run this command the first time to build and start the cluster.
  docker-compose up -d          # Use this command to start the cluster after the initial build (not needed immediately after the first build since the cluster will already be running).
  docker-compose stop           # Stop the running cluster.
  docker-compose down           # Shut down and remove all containers in the cluster.
  ```

  The -d flag runs the containers in detached mode, meaning they will run in the background.
  

* After starting the containers, verify that the Spark cluster is up and running by opening the Spark Web UI in your browser::
  ```  
  http://localhost:8080/
  ```
  You should see the Spark master web interface, indicating that your multi-node Spark cluster is running correctly.


* Additional configurations:

  - All secret keys, credentials, and other sensitive information should be stored in a dedicated secrets folder. This folder should be mounted to each container using Docker volumes, as specified in the docker-  compose.yml file.
  - In the config.py file present in the config sub-directory (in the scripts directory), paths for the bucket_name, files and service account file path will be given. These can be changed as required.


#### Note
In the ```scripts``` directory, there are Python scripts with PySpark code, including:
- ```simple_spark_job.py``` -> A basic PySpark application that creates a dummy DataFrame and performs aggregations on it.
- ```read_from_gcp.py``` -> An application that reads files from a Google Cloud Storage (GCS) bucket and performs aggregations on the data.

Additionally, custom scripts can be created and added to this directory as needed.

### Run commands:
All run commands are available in the ```commands.sh``` file. 

### Cluster Configurations:
Changes to the cluster can be made by modifying the ```docker-compose.yml``` file. For instance, you can increase the number of workers by adding more instances of the worker configuration in the file.
  
### Conclusion
You have successfully set up a multi-node Spark cluster locally using Docker and Docker Compose. You can now use this environment for simulating distributed data processing activities.
