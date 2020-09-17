import tensorflow as tf 
from tensorflow.keras.preprocessing import image
import numpy as np 

def getLabel(n):
    LABELS = {'PNEUMONIA': 0, 'NORMAL': 1, 'COVID19': 2}    
    for key, val in LABELS.items():
        if n == val:
            return key
    return -1


# 예측 함수
def diseasePredict(img_path):
    base_model_path = r"boards\ml\DenseNet_base_model.h5"
    model_path = r"boards\ml\DenseNet_model.h5"

    base_model = tf.keras.models.load_model(base_model_path)
    model = tf.keras.models.load_model(model_path)

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    pred = base_model.predict(img_tensor)
    result = model.predict(pred)

    code = np.argmax(result,axis=1)

    disease = getLabel(code)

    return disease



# 주연
# from tensorflow.keras.models import load_model
# import tensorflow as tf
# import pandas as pd
# import numpy as np
# import PIL.Image as Image
# import matplotlib.pyplot as plt
# import cv2
# import tensorflow_hub as hub

# def prediction(image):
#     # yourmodel = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_model.h5"
#     # f_model = r"C:\Users\Lagom\lagom\CXR_AI\3. WEB\sample\XCR\board\ml\resnet_feature_model.h5"
#     yourmodel = r'..\..\..\..\..\2. ML\efficientnet_model1.h5'
#     f_model = r'..\..\..\..\..\2. ML\efficientnet_f_model1.h5'

#     model = load_model(yourmodel)
#     img = cv2.imread(image)
#     img = cv2.resize(img, dsize=(224,224))
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)
#     feature_model = tf.keras.models.load_model((f_model),custom_objects={'KerasLayer':hub.KerasLayer})
#     feature_vector = feature_model.predict(img)
#     prediction = model.predict(feature_vector)[0]
#     unique_sorted_Y = ['COVID19','NORMAL','PNEUMONIA']
#     top_3_predict = prediction.argsort()[::-1]
#     labels = [unique_sorted_Y[index] for index in top_3_predict]

#     # print(labels[0])

#     return labels[0]

# # 진균
# import numpy as np
# import tensorflow as tf
# from keras.models import load_model

# # 한번에 하나의 이미지만 예측할 수 있다.

# def inception_resnt_predict_CXR(image_path):
#     # 모델 불러오기
#     # 모델 불러올 때 Warning이 표시될 수 있는데 이는 더 training하지 못한다는 의미이고,
#     # 이 함수에서는 더 이상 training을 하지 않음.
#     model_path = r'C:\Users\wjdwl\Desktop\covid_model\CXR_AI\3. WEB\sample\XCR\board\ml\covid_model_size299_best.h5'
#     # r'C:\Users\wjdwl\Desktop\covid_model\CXR_AI\2. ML\Inception_Resnet_V2_224_best.h5'
#     feature_model_path = r'C:\Users\wjdwl\Desktop\covid_model\CXR_AI\3. WEB\sample\XCR\board\ml\Inception_Resnet_feature_model299.h5'

#     model = load_model(model_path)
#     feature_model = load_model(feature_model_path)
#     # 이미지를 불러옴
#     img = cv2.imread(image_path)
#     # 이미지 크기를 모델에 맞게 조정
#     img = cv2.resize(img, dsize=(299,299))
#     # 이미지 픽셀값 스케일링
#     img = img / 255.0
#     # 이미지 차원 확장 (224,224,3) -> (1,224,224,3)  : feature_model에 넣기위함
#     img = np.expand_dims(img, axis=0)
#     # feature_model에서 feature 추출
#     feature_vector = feature_model.predict(img)
#     # 앞서 생성한 model 분류기를 통해 예측 수행/ [[]]이므로 0번인덱스만 뽑아서 1차원으로 가져옴
#     prediction = model.predict(feature_vector)[0]
#     unique_sorted_Y = ['COVID19','NORMAL','PNEUMONIA']
#     # 가장 예측값이 높은 인덱스를 반환
#     index = prediction.argmax()

#     # labels에 저장 
#     label = unique_sorted_Y[index]
#     # print(label)
#     return label
