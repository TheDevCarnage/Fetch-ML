import os
 
import numpy as np
import tensorflow as tf
from datetime import datetime
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


model_path = "../model/"
loaded_model = tf.keras.models.load_model(model_path)


app = FastAPI()
templates = Jinja2Templates(directory="templates")



@app.get("/predict", response_class=HTMLResponse)
async def predict_form(request: Request):
    return templates.TemplateResponse("predictions.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict_(request: Request, date = Form(...)):
    
    data = date 
    input_date = datetime.strptime(str(data), "%Y-%m-%d").date()
    week_of_year = input_date.isocalendar().week
    quarter = (input_date.month - 1) // 3 + 1
    year = input_date.year  
    month = input_date.month  
    day_of_week = input_date.weekday() 
    year_month = int(input_date.strftime('%Y%m'))
    test_data = np.array([week_of_year, quarter, year,
                          month, day_of_week, year_month])
    predictions = loaded_model.predict(test_data.reshape(1,-1))

    
    return templates.TemplateResponse("predictions.html", {"request": request, "predictions": predictions[0][0]})
