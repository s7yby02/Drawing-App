from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os
import tensorflow as tf
import cv2

app = Flask(__name__)
model_path = os.path.join(os.getcwd(), 'web/Model')
model = tf.keras.models.load_model(model_path)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
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
    # Get the screenshot from the request
    screenshot = request.files['screenshot']

    # Convert the screenshot to a PIL Image
    image = Image.open(screenshot.stream)
    
    processed_image = preprocess(image)
    prediction = model.predict(processed_image)
    label = np.argmax(prediction)
    print(prediction)
    label = np.argmax(prediction)
    print(label)
    print(prediction_dict[label])
    # Return the prediction result
    return {'prediction': prediction_dict[label]}

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

if __name__ == '__main__':
    app.run(debug=True)