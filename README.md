# <center> Drawing App for prediction </center>
## <center> Data Mining Project </center>

## Table of Contents
- ### [Team Members](#team-members)
- ### [Overview](#overview)
- ### [Technologies Used](#technologies-used)
- ### [Data Mining Process](#data-mining-process)

### Team Members
- [ASKRI Aymane](https://github.com/Ayasgo)
- [ELHARRAN Ayoub](https://github.com/s7yby02)

### Overview
This is a project that consists of building a web application where you can draw(via the HTML Canvas element) and let the app predict what you've drawn using AI. 

We used the famous pre-trained model called **[MobileNetV2]("https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4")** that we have re-trained using our own dataset (`Tranfert learning technique`) that consists of drawings of 8 shapes: `car, fish, house, tree, bicycle, guitar, pencil, clock` in the format of JSON files that contains the strokes of the drawings(`the coordinates of the points that the user has drawn`).

The app is built using Flask python framework for the backend and HTML, CSS, and JavaScript for the frontend.

## Used Technologies
- ### Front End
  - **HTML-CSS-JS**

   <center><img src="https://miro.medium.com/v2/resize:fit:5120/1*l4xICbIIYlz1OTymWCoUTw.jpeg" alt="Front End" width="300" height="200"></center>

   Frontend development encompasses the creation of the user interface and user experience on the web. ***HTML*** serves as the building blocks, structuring content, while ***CSS*** styles and formats it, defining layout and visual presentation. ***JavaScript*** adds dynamic behavior, facilitating interactive features and real-time updates. Responsive design ensures adaptability across diverse devices.
- ### BackEnd 
  - **Flask**

   <center> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe3XOWFt0Dz3-UsPhsl6LywSb1tFhx8cInE4y9vZww2w&s" alt="Spring Boot" width="300" height="100"></center>
     
   *Flask* is a lightweight WSGI web application framework in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

   - **Docker**
   <center><img src="https://www.zadara.com/wp-content/uploads/docker.png" alt="FastApi" width="200" height="150" ></center>

   ***Docker*** is a set of platform-as-a-service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries, and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating system kernel and are thus more lightweight than virtual machines. Containers are created from images that specify their precise contents. Images are often created by combining and modifying standard images downloaded from public repositories.
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
   ```json
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
   In this section, we prepared the data so that we can use it easily in the cleaning and preprocessing steps and building the models at the end. 

   We first loaded the data from the JSON files and then eliminated the unnecessary attributes: **name attribute**and modifying the **session attribute**. All that is well structured and explained in the `data_preparation.ipynb` notebook.

   After that, in the `data_cleaning.ipynb` notebook, we cleaned the data by removing the drawings that are wrongs and doesn't match its class. 


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git


