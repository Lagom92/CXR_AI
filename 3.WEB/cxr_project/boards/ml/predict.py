# import tensorflow as tf 
# import numpy as np 
# import cv2

# def getLabel(n):
#     LABELS = {'PNEUMONIA': 0, 'NORMAL': 1, 'COVID19': 2}    
#     for key, val in LABELS.items():
#         if n == val:
#             return key
#     return -1


# # 예측 함수
# def diseasePredict(file_path):
#     ml_path = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\densenet_.h5"

#     image = cv2.imread(file_path)
#     image = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)

#     reshaped_image = image.reshape((-1, 224, 224, 3))

#     model = tf.keras.models.load_model(ml_path)

#     pred = model.predict(reshaped_image)
#     pred_code= np.argmax(pred,axis=1)

#     disease = getLabel(pred_code)

#     return disease



# 모델 임포트
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow import keras
import numpy as np
import tensorflow_hub as hub
from .prediction_and_heatmap_function import get_img_array,make_gradcam_heatmap,gamma_correction,show_CAM,predict_CXR

# 주연
def prediction(image):
    # yourmodel = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_model.h5"
    # f_model = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_feature_model.h5"
    yourmodel = r'boards\ml\efficientnet_model1.h5'
    f_model = r'boards\ml\efficientnet_f_model1.h5'

    model = load_model(yourmodel)
    # 이미지 불러오기 및 이미지 크기 조정
    img = keras.preprocessing.image.load_img(image, target_size=(224,224))
    # 이미지를 array로 변경
    img = keras.preprocessing.image.img_to_array(img)
    # 각 픽셀값을 0과 1사이의 값으로 조정
    img = img / 255.0
    # 모델의 인풋 타입에 맞게 차원을 하나 늘림
    img = np.expand_dims(img, axis=0)
    
    feature_model = tf.keras.models.load_model((f_model),custom_objects={'KerasLayer':hub.KerasLayer})
    feature_vector = feature_model.predict(img)
    prediction = model.predict(feature_vector)[0]
    unique_sorted_Y = ['COVID','NORMAL','PNEUMONIA']
    #확률의 예측값을 5개 선출 
    # 가장 예측값이 높은 인덱스를 반환
    index = prediction.argmax()
    # labels에 저장 
    label = unique_sorted_Y[index]

    return label

# 진균

# 예측함수
# opencv의 resize에서 오류가 발생하여 keras.preprocessing.image의 함수들을 사용하였다.
def inception_resnt_predict_CXR_and_heatmap(image_path):
    
    # 모델 불러오기r"boards\ml\DenseNet_base_model.h5"
    model_path = r'boards\ml\inception_Resnet_model299_best.h5'
    feature_model_path = r'boards\ml\Inception_Resnet_feature_model299.h5'

    model = load_model(model_path)
    feature_model = load_model(feature_model_path)

    # 예측
    prediction = predict_CXR(image_path, model, feature_model)

    # Generate class activation heatmap
    heatmap = make_gradcam_heatmap(image_path, model, feature_model)

    # Class Activation Map with image
    cam_image = show_CAM(image_path, heatmap, prediction)


    return prediction, cam_image

