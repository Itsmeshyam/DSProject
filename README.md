# DSProject - Assignment 1

## Objective
The goal of this project is to use Docker, Kubernetes, and GitHub to create and implement a distributed system. In addition to learning version control and teamwork, the objective is to give practical experience in developing, overseeing, and implementing distributed applications. This system consists of a MongoDB database, a Python-based backend, and a responsive web frontend that are all orchestrated with Kubernetes and containerized with Docker.

## Table of contents
- [Project Overview] (project-overview)
- [Technologies Used] (technologies-used)
- [Project Setup] (project-setup)
- [Directory Structure] (directory-structure)
- [Features](features)
- [API Endpoints] (api-endpoints)
- [Version Control] (version-control)
- [Monitoring and Logging] (monitoring-and-logging)
- [Challenges and Lessons Learned] (challenges-and-lessons-learned)
- [Contributors](contributors)
- [Acknowledgements](acknowledgements)

## Project Overview
The distributed web application used in this project has the following features:


- A **frontend** for user interface, built with HTML and CSS.
- A **backend** with RESTful APIs that was created with Python **Flask**.
- A **MongoDB** database for data storage and management.
- **Docker** for containerizing the backend, frontend, and database services.
- **Kubernetes** for resource management, deployment and orchestration.
- **Github** for teamwork and version control.


## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Version Control**: GitHub
- **Monitoring and Logging**: Prometheus, Grafana (optional)


## Project Setup

### 1. Clone the Repository
To get started, clone the repository to  local machine:
```bash
git clone https://github.com/Itsmeshyam/DSProject.git
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2. Set Up the Frontend

•	Open index.html in your browser after navigating to the frontend/templates folder to see the responsive web interface.
•	The frontend/static folder contains the style.css file, which houses all of the CSS needed for the frontend design.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 3. Set Up the Backend
•	Ensure Python and the required packages are installed (Flask, pymongo).
•	Navigate to the backend folder and install the dependencies: 

```bash
pip install -r requirements.txt

•	Update the backend configuration (app.py) to include the right mongoDB connection details:

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://username:password@host:port/database_name')
db = client.get_database('database_name')
collection = db.get_collection('collection_name')

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 4. Set Up MongoDB

-- Create a MongoDB instance using docker:

```bash

docker run -d -p 27017:27017 --name mongo -e MONGO_INITDB_ROOT_USERNAME=username -e MONGO_INITDB_ROOT_PASSWORD=password mongo

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 5. Run Locally
To run the Flask application locally:

```bash

python app.py
app should now be running at http://localhost:5000.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Directory Structure

distributed-systems/
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── frontend/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
├── kubernetes/
│   ├── frontend-deployment.yaml
│   ├── backend-deployment.yaml
│   └── mongodb-deployment.yaml
└── README.md
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Features

1. Responsive Web Interface: The frontend is built with HTML and CSS, and supports mobile responsiveness.
2. User Input Validation: Client-side validation is handled via HTML forms to ensure proper data entry.
3. API Integration: The backend provides RESTful APIs to interact with the frontend and manage user data.
4. Database Integration : MongoDB is used as the database to store and retrieve user data.
5. Error Handling: Proper error handling is implemented in the backend to manage failed API calls and database connections.
6. Duplicate Email Prevention: Duplicate emails are not allowed in the database. If the same email is submitted, a validation error will be shown.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### API Endpoints

*** POST /submit

•	Request Body: 
o	name: The user's name.
o	email: The user's email.

•	Response: 
o	Success: {"message": "Data Submitted Successfully!"}
o	Error: {"error": "All fields are required!"} or {"error": "Request must be in JSON format!"}
o	Duplicate email: {"error": "Email already exists!"}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Version Control
•	All code is managed using GitHub.
•	Branching Strategy:
  • main – Stable release branch
  • feature/* – New features
  • bugfix/* – Fixes
• Pull requests are used for code reviews and merging.
• Commit messages follow best practices (<type>: <message>).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 6. Docker Setup

--- a. Create Dockerfiles


***Frontend Dockerfile (Dockerfile-frontend):


FROM nginx:alpine
COPY ./frontend/templates /usr/share/nginx/html
COPY ./frontend/static /usr/share/nginx/html/static
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

***Backend Dockerfile (Dockerfile-backend):


FROM python:3.9
WORKDIR /app
COPY ./backend /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

***Database Dockerfile (Dockerfile-database):


FROM mongo
EXPOSE 27017


--- b. Build and Run Containers

After creating the Dockerfiles, we can build and run the Docker containers.

```bash
docker build -f Dockerfile-frontend -t frontend .
docker build -f Dockerfile-backend -t backend .
docker build -f Dockerfile-mongodb -t mongodb .


*** Run the containers:

```bash
docker run -p 80:80 frontend
docker run -p 5000:5000 backend
docker run -p 27017:27017 mongodb

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7. Kubernetes Setup

*** a. Create Kubernetes YAML Files

Next, we need to write Kubernetes deployment YAML files for the frontend, backend, and database services.

--- Frontend Deployment (frontend-deployment.yaml):


apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: frontend:latest
        ports:
        - containerPort: 80


--- Backend Deployment (backend-deployment.yaml):

apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: backend:latest
        ports:
        - containerPort: 5000


--- Database Deployment (database-deployment.yaml):


apiVersion: apps/v1
kind: Deployment
metadata:
  name: database-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: database
        image: database:latest
        ports:
        - containerPort: 1433

*** c. Apply YAML Configurations
We can apply these YAML files using the following command:

```bash

kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/database-deployment.yaml

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 8. Monitoring and Logging

• Prometheus: Collects metrics and monitors application health.
• Grafana: Provides visual dashboards for system performance.
• Kubernetes Logs: Use kubectl logs to view logs for debugging.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 9. Contributors
•	[Your Name] – Role and contribution to the project.
•	[Teammate 1 Name] – Role and contribution to the project.
•	[Teammate 2 Name] – Role and contribution to the project.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 10. Challenges and Lessons Learned

• Docker Networking: Managing communication between containers.
• MongoDB Configuration: Setting up secure access and connections.
• Kubernetes Resource Management: Understanding pods, deployments, and services.
• Persistent Storage: Configuring storage volumes for MongoDB.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 11. Acknowledgements
We want to express our gratitude.

• MongoDB for database solutions.
• Docker and Kubernetes for containerization and orchestration.
• Course instructors for their guidance and feedback.


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

