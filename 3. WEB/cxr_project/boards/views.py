from django.http import request
from django.shortcuts import render, redirect
from .models import Xray
# from .ml.predict import diseasePredict, prediction,inception_resnt_predict_CXR
from .ml.predict import diseasePredict


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
    if xray.prediction is None:
        predict = diseasePredict(xray.photo.path)
        xray.prediction = predict
        xray.save()

    context = {
        'title': xray.title,
        'photo': xray.photo,
        'predict': xray.prediction,
    }

    return render(request, 'result.html', context)