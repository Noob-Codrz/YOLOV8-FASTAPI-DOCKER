from fastapi import FastAPI,HTTPException,UploadFile,File
import io
from io import BytesIO
from ultralytics import YOLO
import pandas as pd
import os
import numpy as np
import cv2
from fastapi.responses import RedirectResponse,StreamingResponse
import json

from Helper.helperFunc import add_BoundingBoxes,get_Images_from_Bytes,get_bytes_from_Images,get_model_predict,save_image



app=FastAPI(title="Detect Plastic")

@app.on_event("startup")
def startupevent():
    if not os.path.exists("Prediction"):
        os.makedirs("Prediction")

    # if not os.path.exists("tmp"):
    #     os.makedirs("tmp")
    print("Start Done") 



@app.get('/')
async def redirect():
    return RedirectResponse("/docs")



@app.post("/predict_to_get_plastics")
async def predict_to_json(file: UploadFile = File(...)):
    model = YOLO("use saample or trained model")
    image = get_Images_from_Bytes(file.file.read())
    predictions = get_model_predict(image, model,flag=True)
    data = json.loads(predictions)
     
    info= {
        "no_of_plastics": len(data),
        "predictions": data
    }
    return info

@app.post("/predict_to_image")
def predict_to_image(file: UploadFile = File(...)):
    model = YOLO("YOLO_Custom_v8m.pt")
    img = get_Images_from_Bytes(file.file.read())
    predictions = get_model_predict(img, model)
    # print(predictions)
    processed = add_BoundingBoxes(predictions, img)
    return StreamingResponse(content=get_bytes_from_Images(processed) , media_type="image/jpeg")

   
@app.post("/predict_save_image")
async def predict_and_save(file:UploadFile=File(...)):
    model=YOLO("use saample or trained model")
    img=get_Images_from_Bytes(file.file.read())
    predictions=get_model_predict(img,model)
    bb_box=add_BoundingBoxes(img,predictions)
    processed_image_bytes=get_bytes_from_Images(bb_box)
    save_image(file_name=file.filename,image=bb_box,prediction=predictions)
    return StreamingResponse(content=processed_image_bytes,media_type="image/jpeg") 


