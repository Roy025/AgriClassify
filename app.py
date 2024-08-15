import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = load_model(r'D:\PRAPTI\Books\PROJECTS\AgriClassify\best_model_keras.keras')

# List of categories
data_cat = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 
            'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 
            'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 
            'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 
            'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 
            'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 
            'turnip', 'watermelon']

# Set image dimensions
img_height = 180
img_width = 180

# Define the upload folder
UPLOAD_FOLDER = os.path.join('uploads')  # Direct uploads folder
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Save the uploaded image
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Load and process the image using the same steps as in Kaggle
            try:
                image = tf.keras.utils.load_img(filepath, target_size=(img_height, img_width))
                img_arr = tf.keras.utils.img_to_array(image)
                img_bat = tf.expand_dims(img_arr, 0)  # Create a batch of one

                # Make a prediction
                predict = model.predict(img_bat)
                score = tf.nn.softmax(predict[0])

                # Get the predicted class and confidence
                predicted_class = data_cat[np.argmax(score)]
                confidence = np.max(score) * 100

                # Print the output in the same format as your Kaggle code
                print('Product in image is {} with accuracy of {:0.2f}'.format(predicted_class, confidence))

                # Pass data to result.html
                return render_template('result.html', 
                                        image=file.filename, 
                                        predicted_class=predicted_class, 
                                        confidence=confidence)

            except Exception as e:
                print("Error processing image:", str(e))
                return "Error processing image: " + str(e)
    
    return render_template('upload.html')

# Route to serve the uploaded image
@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
