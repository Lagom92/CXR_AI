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