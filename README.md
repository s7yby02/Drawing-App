# <center> Drawing App for prediction </center>
## <center> Data Mining Project </center>

## Table of Contents
- [Team Members](#team-members)
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Used Technologies](#used-technologies)
  - [Front End](#front-end)
  - [BackEnd](#backend)
  - [AI model](#ai-model)
- [Data Mining Process](#data-mining-process)
  - [Data Selection](#data-selection)
  - [Data Understanding](#data-understanding)
  - [Data Preparation](#data-preparation)
   - [Feature Engineering](#feature-engineering)
   - [Model Building & evaluation](#model-building--evaluation)
- [Installation](#installation)
   - [The API](#the-api)
   - [The Web App](#the-web-app)

### Team Members
- [ASKRI Aymane](https://github.com/Ayasgo)
- [ELHARRAN Ayoub](https://github.com/s7yby02)

### Overview
This is a project that consists of building a web application where you can draw(via the HTML Canvas element) and let the app predict what you've drawn using AI. 

We used the famous pre-trained model called **[MobileNetV2]("https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4")** that we have re-trained using our own dataset (`Tranfert learning technique`) that consists of drawings of 8 shapes: `car, fish, house, tree, bicycle, guitar, pencil, clock` in the format of JSON files that contains the strokes of the drawings(`the coordinates of the points that the user has drawn`).

The app is built using Flask python framework for the backend and HTML, CSS, and JavaScript for the frontend.

### Project Structure
The project is structured as follows:
```bash	
Drawing-App
│
└──ML_approach
│ │ Data_preparation.ipynb
│ │ Data_cleaning.ipynb
│ │ Feature_Extraction.ipynb
│ │ features.py
│ │ Model.ipynb
└──DL_approach
│ │ Data_preprocessing.ipynb
│ └──the model # the deep learning model that we have trained
└──data # the original dataset
│ │ 
│ └───raw
│ │ │ 1663053145814.json #the files that contains the drawings
│ │ │ ...
└──newdata # the dataset after the data preparation
│ │
│ └───json
│ │ │ 0.json # the dataset in json format after preparing it
│ │ │ ...
│ │
│ └───csv
│ │ │ data.csv # the dataset in csv format after extracting the features
│ │ 
│ └───imgs
│ │ │ 0_bicycle.png # the images that we have created from the drawings
│ │ │ ...
│ │
│ └───resized_clean_imgs_crop # the images that we have created from the drawings after cleaning them
│ │ │ 0_bicycle.png
│ │ │ ...
└──web
│ │
│ └───templates
│ │ │ index.html
│ └───static
│ │ │ styles.css
│ │ │ scripts.js
| └───the model # the deep learning model that we have trained
│ │ main.py
│ │ requirements.txt # the dependencies of the web app
└───api
│ │ app.py
│ └───the model # the deep learning model that we have trained
│ │ requirements.txt # the dependencies of just the api without backend and frontend 
│ README.md
```
   ### NB. Each folder or file that is not mentioned in the structure is not important for the understanding of the project.

## Used Technologies
- ### Front End
  - **HTML-CSS-JS**

   <center><img src="https://miro.medium.com/v2/resize:fit:5120/1*l4xICbIIYlz1OTymWCoUTw.jpeg" alt="Front End" width="300" height="200"></center>

   Frontend development encompasses the creation of the user interface and user experience on the web. ***HTML*** serves as the building blocks, structuring content, while ***CSS*** styles and formats it, defining layout and visual presentation. ***JavaScript*** adds dynamic behavior, facilitating interactive features and real-time updates. Responsive design ensures adaptability across diverse devices.
- ### BackEnd 
  - **Flask**

   <center> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe3XOWFt0Dz3-UsPhsl6LywSb1tFhx8cInE4y9vZww2w&s" alt="Spring Boot" width="300" height="100"></center>
     
   *Flask* is a lightweight WSGI web application framework in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

- ### AI model 
   - **Jupyter Notebook**
   
      <center> <img src="https://miro.medium.com/v2/resize:fit:1358/1*RzxZF0mmXAsMLrIzAWYDSg.png" alt="Jupyter Notebook" width="300" height="150"></center>
     
      ***Jupyter Notebook*** is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
   - **TensorFlow&Keras**
   
      <center> <img src="https://3.bp.blogspot.com/-QZVBl08fmPk/XhO909Ha1dI/AAAAAAAACZI/q1a1UykGKe0KDUZ_ZITtWmM7bBJFRrvPQCLcBGAsYHQ/s1600/tensorflowkeras.jpg" alt="TensorFlow&Keras" width="300" height="150"></center>

      ***TensorFlow & Keras*** are open-source machine learning tools. TensorFlow supports deep and traditional machine learning, using computational graphs for complex computations. Keras, integrated into TensorFlow since version 2.0, is a high-level API for building and training neural networks. It simplifies the construction of neural networks, allowing rapid prototyping and runs seamlessly on various deep learning frameworks, primarily TensorFlow.       

  - **FastApi**

    <center><img src="https://camo.githubusercontent.com/580b7032c938b3cbf4f2547383a8d43d86aba159622747f1993b0e45c04f0665/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67" alt="FastApi" width="400" height="150" ></center>

      ***FastAPI*** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is inspired by APIStar, but it is not a fork. It is designed to be high-performance, asynchronous, and ready to serve production workloads. It is powered by Starlette and Pydantic. It is a class-based API framework that is built on top of Starlette, which is a lightweight ASGI framework/toolkit. It is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is inspired by APIStar, but it is not a fork. It is designed to be high-performance, asynchronous, and ready to serve production workloads. It is powered by Starlette and Pydantic. It is a class-based API framework that is built on top of Starlette, which is a lightweight ASGI framework/toolkit.

## Data Mining Process
- ### Data Selection
   We utilized a dataset of hand-drawn shapes, which was created by a YouTuber who asked his followers to sketch eight different shapes for him. The collected data was then stored in the form of JSON files.
- ### Data Understanding
   The dataset consists of 8 classes: `car, fish, house, tree, bicycle, guitar, pencil, clock`. Each class contains a set of drawings, where each drawing is represented by a list of strokes. Each stroke is a list of points, where each point is a list of two values representing the x and y coordinates of the point.

   So the dataset is structured as follows:
   ```bash
   {
      "session": 1663053145814,
      "student": "Aymane",
      "drawings": {
         "car": [
            [
               [x11, y11],
               [x12, y12],
               ...
            ],
            [
               [x21, y21],
               [x22, y22],
               ...
            ],
            ...
         ],
         "fish": [
            ...
         ],
         ...
      }
   }
   ```
   The session and the name attributes are just for identification purposes, while the drawings attribute contains the actual data.
- ### Data Preparation
   In this section, we prepared the data so that we can use it easily in the cleaning and preprocessing steps and when building the models at the end. 

   We first loaded the data from the JSON files and then eliminated the unnecessary attributes: **name attribute**and modifying the **session attribute**. All that is well structured and explained in the `data_preparation.ipynb` notebook inside the `ML_approach` folder.

   After that, in the `data_cleaning.ipynb` notebook, we cleaned the data by removing the drawings that are wrongs and doesn't match its class. 
- ### Feature Engineering
   In this section, given that we have raw JSON data, it was necessary for us to identify and extract features that would assist us in distinguishing between classes. This was done with the aim of constructing the model from this data independently.

   These are the features that we extracted from the raw data:
   - **Point Count**: The total count of points required to draw the shape.
   - **Path Count**: The total number of lines required to draw the shape.
   - **width**: The horizontal dimension of the shape.
   - **height**: The vertical dimension of the shape.
   - **elongation**: The extent to which a shape stretches in one direction compared to its orthogonal direction.
   - **roundness**: The degree to which the shape of an object resembles a perfectly round circle.
   - **area**: The total space enclosed within the shape.

   The feature engineering process is done in the `Feature_Extraction.ipynb` notebook and all the features extractor functions are in the `features.py` file.

- ### Model Building & evaluation
   In this section, we tried different Machine Learning models to predict the drawings. We used the extracted features to train the models. We tried different models like `Random Forest, Decision Tree, KNN, SVM and Logistic Regression`. 
   
   The model was built and trained in the `model_building.ipynb` notebook.

   Despite our efforts in training the models, we were unable to achieve satisfactory accuracy (not exceeding 61%). As a result, we opted for a **Deep Learning Approach** over basic Machine learning models. 
   
   Specifically, we utilized a pre-existing model known as `MobileNetV2`, which we retrained with our unique dataset (we converted the JSON files into image plots and saved these plots as images). The retraining of the model was accomplished using the `Transfer Learning` technique.

   All the process is well explained in the `Data_preprocessing.ipynb` notebook inside the `DL_approach` folder.



## Installation
The project is divided into two parts: **the API** and **the Web App** in case you want to test just the API without the frontend and the backend. The API is used to predict the drawings and the Web App is used to draw the shapes and see the predictions. 

The API is built using FastAPI and the Web App is built using Flask.

First, you need to clone the repository:

   ```bash
   git clone https://github.com/s7yby02/Drawing-App.git
   ```

- ### The API
   To install the API, you need to install the dependencies first. You can do this by running the following command:

   ```bash
   cd Drawing-App/api
   pip install -r requirements.txt
   ```

   After installing the dependencies, you can run the API by running the following command:

   ```bash
   uvicorn app:app --reload
   ```

   The API will be running on `http://127.0.0.1:8000`.

- ### The Web App
   To install the Web App, you need to install the dependencies first. You can do this by running the following command:

   ```bash
   cd Drawing-App/web
   pip install -r requirements.txt
   ```

   After installing the dependencies, you can run the Web App by running the following command:

   ```bash
   python main.py
   ```

   The Web App will be running on `http://127.0.0.1:5000`.

   You can now draw the shapes and see the predictions.

- ## Quick Demo
   Here is a quick demo of the Web App:

   ![App demo](imgs_for_notebooks/demo.gif)
   