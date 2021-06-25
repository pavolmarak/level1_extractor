import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow_estimator.python.estimator.canned.timeseries import model

def loadModel():
    global model 
    model_path ='/home/editav/4_triedy_0.98.h5'
    model = tf.keras.models.load_model(model_path)


def trainedScript(item):
    image = [item]
    train_mean = np.mean(image)
    train_std = np.std(image)
    image_arch = (image - train_mean) / train_std
    predictions = model.predict(image_arch)
    return np.argmax(predictions[0])












