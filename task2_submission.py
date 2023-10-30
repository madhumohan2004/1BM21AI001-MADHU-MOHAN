import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

def main():
    # Define the path to your dataset directory
    dataset_dir = "testlabelling"

    # Initialize lists to store images and labels
    images = []
    labels = []

    # Define a function to extract the kill count label from a text file
    def extract_coordinates_from_txt(txt_file):
        # Initialize a list to store the extracted coordinates
        coordinates = []

        # Read the line from the specified text file
        txt_file_path = os.path.join(dataset_dir, txt_file)
        with open(txt_file_path, 'r') as file:
            line = file.read().strip()
        
        # Split the line into individual coordinate values
        coordinate_values = line.split()  # Assumes coordinates are space-separated

        # Convert each coordinate value to an integer and add to the list
        for value in coordinate_values:
            coordinates.append(int(value))
        
        return coordinates

    # Load images and labels from the dataset
    for image_file in os.listdir(dataset_dir):
        if image_file.endswith(".jpg"):  # Assuming your images are in JPG format
            img_path = os.path.join(dataset_dir, image_file)
            image = cv2.imread(img_path)  # Load the image using OpenCV or your preferred library
            label = extract_coordinates_from_txt("killcrd.txt")  # Call the function to parse the coordinates from the text file
            images.append(image)
            labels.append(label)

    # Convert lists to NumPy arrays
    images = np.array(images)
    labels = np.array(labels)

    # Split the dataset into training and testing sets
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

    # Define your neural network model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(image_height, image_width, 3)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(num_classes, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    num_epochs = 10


    # Train the model on the training dataset
    model.fit(train_images, train_labels, epochs=num_epochs)

    # Evaluate the model on the testing dataset
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print(f"Test accuracy: {test_acc}")

    # Make predictions on new data (similar to the inference step)

    # Deploy the trained model in your application or system for image classification

if __name__ == "__main__":
    main()
