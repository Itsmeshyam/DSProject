# Health Registration Form - Distributed System Deployment
Project Overview

This project demonstrates the deployment of a health registration form for students using Docker, Kubernetes, and GitHub. It focuses on containerization, orchestration, and efficient data management while providing hands-on experience with version control, distributed systems, and cloud-native technologies.

Features

User registration form collecting username, email, address, phone number, student ID, and message.

Data storage in MongoDB for scalable and efficient data management.

Containerized deployment using Docker for portability.

Kubernetes-based orchestration ensuring high availability and scalability.

Monitoring and logging with Grafana for real-time insights.

Project Workflow

# 1. Local Testing and Dockerization

After thoroughly testing the application locally, we create a Docker image using a Dockerfile. The image is then tested locally to ensure that all functionalities work correctly. Once verified, we tag the image and push it to Docker Hub, making it accessible for deployment.

Build Docker Image
docker build -t health-registration-form .

Run the container locally
docker run -p 5000:5000 health-registration-form

Tag the image
docker tag health-registration-form username/health-registration-form:v1

Push the image to Docker Hub
docker push username/health-registration-form:v1

# 2. Kubernetes Deployment

We use a YAML configuration file to define the deployment settings, specifying the Docker image name, replicas, resource limits, and environment variables. Kubernetes then pulls the image from Docker Hub and deploys it in a Kubernetes cluster, ensuring a stable and scalable containerized environment.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: health-registration
spec:
  replicas: 2
  selector:
    matchLabels:
      app: health-registration
  template:
    metadata:
      labels:
        app: health-registration
    spec:
      containers:
      - name: health-registration-container
        image: username/health-registration-form:v1
        ports:
        - containerPort: 5000

To apply the deployment:

kubectl apply -f deployment.yaml

# 3. Monitoring and Logging

For system health monitoring and logging, we integrate Grafana, which provides real-time insights into resource utilization, performance, and application health.

System metrics include CPU, memory, network usage, and container health.

Custom dashboards provide an intuitive overview of the application's performance.

Integrated with Prometheus to collect and visualize data.

# Screenshots

Screenshot of the application’s home page.

![Screenshot 2025-03-10 201024](https://github.com/user-attachments/assets/4c660332-296c-4013-8077-b76011fc29a6)

Screenshot showing MongoDB database entries after data processing.
![mongodb 1](https://github.com/user-attachments/assets/960b11ed-df1e-433b-b573-9098491a838c)

Screenshot of the Docker image stored in Docker Hub.
![docker](https://github.com/user-attachments/assets/338f30cc-c098-40c0-847a-fe5424b92a71)

Screenshot of Grafana dashboard displaying real-time monitoring metrics.
![WhatsApp Image 2025-03-10 at 19 45 02_48c0a95f](https://github.com/user-attachments/assets/2f7ebe44-5cb9-4930-9372-5f341e129a15)


# Technologies Used

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Database: MongoDB

Containerization: Docker

Orchestration: Kubernetes

Monitoring & Logging: Grafana

# License

This project is licensed under the MIT License - see the LICENSE file for details.

