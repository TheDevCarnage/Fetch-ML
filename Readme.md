# Fetch Machine Learning Model and API

## Introduction

This project involves creating a Machine Learning (ML) model for predicting certain outcomes based on date data and deploying it as an API using FastAPI. The API will accept a date as input and provide predictions using the trained ML model. Additionally, it offers a user-friendly HTML template for interacting with the API.

## Requirements

Before you begin, make sure you have the following requirements installed:

- Python (version X.X)
- Docker (if you plan to use Docker for deployment)
- Git (optional)

## Setup

### 1. Clone the Repository

If you're using Git, clone the project repository to your local machine:

```bash
git clone <repository_url>
cd fetch-ml
```

Alternatively, you can download the project as a ZIP file from the repository.

### 2. Create a Virtual Environment

To create a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Change to the API Directory

Change your working directory to the API folder:

```bash
cd api
```

### 5. Run the FastAPI App

To run the FastAPI app locally, use the following command:

```bash
uvicorn main:app --reload
```

The FastAPI app will be accessible at `http://localhost:8000`.

## Interacting with the API

The API includes a user-friendly HTML template for making predictions based on date inputs. To access the HTML template, open a web browser and navigate to:

`http://localhost:8000/predict`

This page provides an input field where you can enter a date. Upon submitting the date, the API will provide predictions and display the results on the page.

## Docker Deployment

If you prefer to run the app in a Docker container, follow these steps:

### 1. Build the Docker Image

From the project's root directory, where the `Dockerfile` is located:

```bash
docker build -t fetch-ml-app .
```

This command builds a Docker image named `fetch-ml-app`.

### 2. Run the Docker Container

After building the image, you can run a Docker container from the image:

```bash
docker run -p 8000:80 fetch-ml-app
```

This command runs a Docker container based on the image you built and maps port 8000 on your host to port 80 in the container.

### 3. Access the FastAPI App

The FastAPI app is now accessible at `http://localhost:8000`. Open a web browser and navigate to this URL to use the HTML template for interacting with the API.
