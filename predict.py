import PIL
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

captcha_width = 150
captcha_height = 50
captcha_depth = 1
label_map_path = "labels.txt"
captcha_model_path = "captcha_model.h5"

# Load the label map
with open(label_map_path, 'r') as f:
    label_map = f.readlines()
label_map = [label.strip() for label in label_map]

# Load the model
captcha_model = load_model(captcha_model_path)

def predict_captcha(image_path):
    # Load the image
    with Image.open(image_path) as img:
        # Resize the image to match the input shape of the model
        img = img.resize((captcha_width, captcha_height), resample=PIL.Image.BILINEAR)
        # Convert the image to grayscale
        img = img.convert('L')
        # Convert the image to a numpy array
        img_array = np.array(img)
        # Normalize the pixel values to be between 0 and 1
        img_array = img_array / 255.0
        # Reshape the image array to match the input shape of the model
        img_array = img_array.reshape((1, captcha_width, captcha_height, captcha_depth))
        
        # Predict the captcha
        captcha_pred = captcha_model.predict(img_array)
        # Convert the predicted output to a string
        captcha_pred_str = ''.join([label_map[i] for i in np.argmax(captcha_pred, axis=1)])
        return captcha_pred_str
    
predicted_captcha = predict_captcha("images\\2p2y8.png")
print(predicted_captcha)