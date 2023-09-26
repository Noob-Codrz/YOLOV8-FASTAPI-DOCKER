# YOLOV8-FASTAPI-DOCKER
Ready to start your object detection journey with YOLOv8-FastAPI? 🚀

## Description
This repository serves as a template for object detection using YOLOv8 and FastAPI. With YOLOv8, you get a popular real-time object detection model and with FastAPI, you get a modern, fast (high-performance) web framework for building APIs. The project also includes Docker, a platform for easily building, shipping, and running distributed applications.

### Sample
Here's a sample of what you can expect to see with this project and also check the Results folder :
<img width=600 src="Results\DJI_0255.jpg_predicted.jpg" alt="">

# What's inside:

- YOLOv8: A popular real-time object detection model
- FastAPI: A modern, fast (high-performance) web framework for building APIs
- Docker: A platform for easily building, shipping, and running distributed applications

 
---
# Getting Started

You have two options to start the application: using Docker or locally on your machine.

## Using Docker
Start the application with the following command:
```
docker build -t container_name .
docker run -p 8000:8000 container_name
```

## Locally
To start the application locally, follow these steps:

1. Install the required packages:

```
pip install -r requirements.txt
```
2. Start the application:
```
python startscript.py
 
```  
*Note: You can change the address and port in the file **docker-file***
  


- 
# Overview of the code
* [main.py]( main.py) - Base FastAPI functions  
* [helperfunc.py](Helper\HelperFunc.py) - YoloV8 functions
* [TestImages]  (Test Images) - For you to test the working  
