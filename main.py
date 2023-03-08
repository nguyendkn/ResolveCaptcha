import os
import PIL
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical

# Set the image width and height
IMAGE_WIDTH = 150
IMAGE_HEIGHT = 50

# Define the function to generate training data
def generate_training_data(images, labels, num_classes):
    # Initialize the training data arrays
    x_train = np.zeros((len(images), IMAGE_WIDTH, IMAGE_HEIGHT, 1), dtype=np.float32)
    y_train = np.zeros((len(images), num_classes), dtype=np.int32)
    for i, image in enumerate(images):
        # Convert the image to grayscale
        image = image.convert('L')
        # Resize the image to the specified width and height
        image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), resample=PIL.Image.BILINEAR)
        # Convert the image to a numpy array and normalize the pixel values to the range [0, 1]
        image = np.asarray(image, dtype=np.float32) / 255.
        # Add the image to the training data array
        x_train[i] = image.reshape((IMAGE_WIDTH, IMAGE_HEIGHT, 1))
        # Convert the label to a one-hot encoding format and add it to the training label array
        y_train[i] = to_categorical(labels[i], num_classes=num_classes)
    return x_train, y_train

# Define the function to build the model
def build_model(input_shape, num_classes):
    # Create a sequential model
    model = Sequential()
    # Add the first convolutional layer with 32 filters, a kernel size of 3x3, and ReLU activation
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    # Add max pooling layer with a pool size of 2x2
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Add the second convolutional layer with 64 filters, a kernel size of 3x3, and ReLU activation
    model.add(Conv2D(64, (3, 3), activation='relu'))
    # Add max pooling layer with a pool size of 2x2
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Flatten the output of the convolutional layers
    model.add(Flatten())
    # Add a fully connected layer with 128 units and ReLU activation
    model.add(Dense(128, activation='relu'))
    # Add the output layer with the specified number of units and softmax activation
    model.add(Dense(num_classes, activation='softmax'))
    # Compile the model with categorical cross-entropy loss, Adam optimizer, and accuracy metric
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Define the main function
def main():
    # Set the path to the captcha images and labels
    captcha_dir = 'images'
    label_file = 'labels.txt'
    # Load the captcha images and labels
    captcha_images = []
    captcha_labels = []
    with open(label_file, 'r') as f:
        for line in f:
            captcha_file, captcha_label = line.strip().split(',')
            captcha_path = os.path.join(captcha_dir, captcha_file) + ".png"
            captcha_image = Image.open(captcha_path)
            captcha_images.append(captcha_image)
            captcha_labels.append(int(captcha_label.strip()))
        # Get the number of classes from the labels
        num_classes = len(set(captcha_labels))
        # Generate the training data
        x_train, y_train = generate_training_data(captcha_images, captcha_labels, num_classes)
        # Build the model
        input_shape = (IMAGE_WIDTH, IMAGE_HEIGHT, 1)
        model = build_model(input_shape, num_classes)
        # Train the model
        model.fit(x_train, y_train, batch_size=32, epochs=100, validation_split=0.2)
        # Save the model
        model.save('captcha_model.h5')

main()
