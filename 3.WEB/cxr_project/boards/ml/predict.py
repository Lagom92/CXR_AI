import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import tensorflow_hub as hub
import cv2
import numpy as np
from .prediction_and_heatmap_function import get_img_array,make_gradcam_heatmap,gamma_correction,show_CAM,predict_CXR
import os
from django.conf import settings

# 주연
def prediction(image):
    yourmodel = r'boards\ml\efficientnet_model1.h5'
    f_model = r'boards\ml\efficientnet_f_model1.h5'

    model = load_model(yourmodel)
    img = keras.preprocessing.image.load_img(image, target_size=(224,224))
    img = keras.preprocessing.image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    feature_model = tf.keras.models.load_model((f_model),custom_objects={'KerasLayer':hub.KerasLayer})
    feature_vector = feature_model.predict(img)
    prediction = model.predict(feature_vector)[0]
    unique_sorted_Y = ['COVID19','NORMAL','PNEUMONIA']
    index = prediction.argmax()
    label = unique_sorted_Y[index]

    return label
#진균
def inception_resnt_predict_CXR_and_heatmap(image_path):
    
    model_name = 'inception_Resnet_model299_best.h5'
    feature_model_name = 'inception_Resnet_feature_model299.h5'

    loaded_model = tf.keras.models.load_model(os.path.join(settings.MODEL_ROOT, model_name))
    loaded_feature_model = tf.keras.models.load_model(os.path.join(settings.MODEL_ROOT, feature_model_name))

    prediction, plot = predict_CXR(image_path, loaded_model, loaded_feature_model)
    heatmap = make_gradcam_heatmap(image_path, loaded_model, loaded_feature_model)

    cam_image = show_CAM(image_path, heatmap, prediction)

    return prediction, cam_image, plot

#시영
def getLabel(n):
    LABELS = {'COVID19': 0, 'NORMAL': 1, 'PNEUMONIA': 2}
    for key, val in LABELS.items():
        if n == val:
            return key


def diseasePredict(image_path):
    model_path = r"boards\ml\Densenet.h5"
    model = tf.keras.models.load_model(model_path)

    img = cv2.imread(image_path)
    img = cv2.resize(img, dsize=(224,224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    code = np.argmax(prediction)
    disease = getLabel(code)

    return disease