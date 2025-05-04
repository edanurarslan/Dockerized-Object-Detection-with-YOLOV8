# Dockerized YOLOv8 Object Detection Microservice

A lightweight, scalable object detection microservice built using **YOLOv8**, **FastAPI**, and optionally containerized with **Docker** and orchestrated via **Docker Compose**.

---

## Project Purpose

This project aims to provide a fast, reusable, and developer-friendly microservice for real-time object detection. It enables users to upload an image and receive detected objects with their bounding boxes and confidence scores.

The service supports optional filtering by object label and can be easily integrated into larger systems thanks to its clear API structure and Docker compatibility.

---

## Target Audience

* Developers and researchers working on computer vision projects.
* ML Ops engineers looking to integrate object detection into microservices.
* Students or hobbyists wanting a production-ready example of YOLOv8 + FastAPI integration.
* Teams deploying scalable AI services via containerization.

---

## Technologies Used

* **[YOLOv8](https://docs.ultralytics.com/)**: A state-of-the-art real-time object detection model from Ultralytics.
* **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast (high-performance) web framework for building APIs with Python 3.10+.
* **[ONNX](https://onnx.ai/)**: Open Neural Network Exchange format for exporting and running the YOLO model efficiently.
* **[Docker](https://www.docker.com/)**: For containerizing the application.
* **[Docker Compose](https://docs.docker.com/compose/)**: For orchestrating the microservice and future extensions.
* **OpenCV, ONNX Runtime, Python Libraries**: For image processing and model inference.

---

## Sample UI & Output

> We'll add screenshots here (e.g., upload form UI and a sample detected image result).

---

## How to Run the Project

You can run the microservice in three different ways:

---

### Option 1: Without Docker (Manual Setup)

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Dockerized-Object-Detection.git
cd Dockerized-Object-Detection
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the FastAPI server**

```bash
cd api_endpoint
uvicorn app:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)
![Homepage Screenshot](microservice.png)

---

### Option 2: Using Docker

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Dockerized-Object-Detection.git
cd Dockerized-Object-Detection
```

2. **Build the Docker image**

```bash
docker build -t yolo-object-detector .
```

3. **Run the container**

```bash
docker run -it --rm -p 8000:8000 yolo-object-detector
```

---

### Option 3: Using Docker Compose

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Dockerized-Object-Detection.git
cd Dockerized-Object-Detection
```

2. **Start the service**

```bash
docker compose up --build
```

3. **Access the web interface**

Visit: [http://localhost:8000](http://localhost:8000)

---

## Testing

Automated tests for object detection can be found in the `object_detection_tests/` directory. Run the test script:

```bash
python test_object_detection.py
```

Each test loads a sample image, sends it to the API, and verifies if the expected object label is detected.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
