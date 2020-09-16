from django.http import request
from django.shortcuts import render, redirect
from .models import Xray
# from .ml.predict import diseasePredict, prediction,inception_resnt_predict_CXR


def main(request):

    return render(request, 'main.html')


# 이미지 요청 
def test(request):

    return render(request, 'test.html')


# 요청된 이미지 저장
def detect(request):
    if request.method == 'POST':
        xray = Xray.objects.create(
            title = request.POST['title'],
            photo = request.FILES['image']
        )

        return redirect('result')

    else:
        return render(request, 'home.html')


# 이미지 확인
def result(request):
    xray = Xray.objects.last()

    # Predict 
    # predict = diseasePredict(xray.photo.path)

    # predict2
    # predict2 = inception_resnt_predict_CXR(xray.photo.path)

    context = {
        'title': xray.title,
        'photo': xray.photo,
        # 'predict': predict,
        # 'predict2': predict2

    }

    return render(request, 'result.html', context)