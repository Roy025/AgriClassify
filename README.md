# Image Classification Web Application
## Project Overview

This project is a web-based image classification application built using Flask and TensorFlow. Users can upload images of fruits or vegetables, and the application will predict the category of the uploaded image and display the result along with the prediction confidence.

## Features
**Image Upload:** Users can upload images from local directory directly through a web interface.
**Real-time Prediction:** The application processes the uploaded image and predicts its category using a pre-trained TensorFlow model.
**Result Display:** The predicted category and confidence level are displayed on a results page along with the uploaded image.
## Project Structure

        project-directory/
        │
        ├── app.py                    
        ├── templates/
        │   ├── result.html            
        │   └── upload.html           
        ├── uploads/                  
        └── README.md                 
## Tech Stack
**Backend:** Flask (Python)
**Machine Learning:** TensorFlow, Keras
**Frontend:** HTML, CSS
**Deployment:** Flask development server

## Installation
### Prerequisites
Python 3.7+
Pip (Python package installer)

### Setup Instructions

#### Clone the repository:

git clone https://github.com/Roy025/AgriClassify.git
cd AgriClassify

#### Create a virtual environment:
python -m venv venv
venv\Scripts\activate

#### Install the required packages:

<!-- pip install tensorflow flask pillow
pip freeze > requirements.txt -->
pip install -r requirements.txt

### Run the application:
python app.py


### Access the application:
Open your web browser and navigate to http://127.0.0.1:5000/.
