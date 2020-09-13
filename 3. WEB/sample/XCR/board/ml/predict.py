import tensorflow as tf 
import numpy as np 
import cv2

def getLabel(n):
    LABELS = {'PNEUMONIA': 0, 'NORMAL': 1, 'COVID19': 2}    
    for key, val in LABELS.items():
        if n == val:
            return key
    return -1


# 예측 함수
def diseasePredict(file_path):
    ml_path = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\densenet_.h5"

    image = cv2.imread(file_path)
    image = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)

    reshaped_image = image.reshape((-1, 224, 224, 3))

    model = tf.keras.models.load_model(ml_path)

    pred = model.predict(reshaped_image)
    pred_code= np.argmax(pred,axis=1)

    disease = getLabel(pred_code)

    return disease



# 주연
from tensorflow.keras.models import load_model
import tensorflow as tf
import pandas as pd
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
import cv2
import tensorflow_hub as hub

def prediction(image):
    yourmodel = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_model.h5"
    f_model = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_feature_model.h5"

    model = load_model(yourmodel)
    img = cv2.imread(image)
    img = cv2.resize(img, dsize=(224,224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    feature_model = tf.keras.models.load_model((f_model),custom_objects={'KerasLayer':hub.KerasLayer})
    feature_vector = feature_model.predict(img)
    prediction = model.predict(feature_vector)[0]
    unique_sorted_Y = ['COVID19','NORMAL','PNEUMONIA']
    top_3_predict = prediction.argsort()[::-1]
    labels = [unique_sorted_Y[index] for index in top_3_predict]

    # print(labels[0])

    return labels[0]