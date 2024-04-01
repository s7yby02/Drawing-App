import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = FastAPI()

@app.get('/')
async def hello_model():
    return {"Hello": "CNN model for drawing application"}

model = load_model('the model')

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    prediction_dict = {
        0: 'car',
        1: 'fish',
        2: 'clock',
        3: 'house',
        4: 'tree',
        5: 'guitar',
        6: 'pencil',
        7: 'bicycle'
    }
    contents = await file.read() # read the image file
    image = Image.open(io.BytesIO(contents))
    processed_image = preprocess(image)
    predictions = model.predict(processed_image)
    label = np.argmax(predictions)
    return JSONResponse(content={
        "prediction": prediction_dict[label]
    })


def preprocess(image):
    if image.mode != 'RGB':
        # print(image.mode)
        image = image.convert('RGB')
        # print(image.mode)
    image = np.array(image)
    input_image_resize = cv2.resize(image, (224,224)) # resizing the image
    input_image_scaled = input_image_resize/255 # scaling the image
    image_reshaped = np.reshape(input_image_scaled, [1,224,224,3]) # reshaping the image to fit in the model input
    return image_reshaped