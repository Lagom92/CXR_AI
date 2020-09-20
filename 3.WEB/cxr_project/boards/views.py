from django.http import request
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from .models import Xray
from .ml.predict import inception_resnt_predict_CXR_and_heatmap , prediction, diseasePredict


def main(request):

    return render(request, 'main.html')

# 이미지 요청 
def test(request):
    if request.method == 'POST':
        xray = Xray.objects.create(
            photo = request.FILES['image'],
        )
        return redirect('result')

    else:
        return render(request, 'test.html')


# 이미지 확인
def result(request):
    xray = Xray.objects.last()
    
    # predict1 = prediction(xray.photo.path)
    # predict3 = diseasePredict(xray.photo.path)
    if not xray.prediction:
        predict, heatmap = inception_resnt_predict_CXR_and_heatmap(xray.photo.path)
        heatmap_io = BytesIO()
        heatmap.save(heatmap_io, format='jpeg')
        heat_file = InMemoryUploadedFile(heatmap_io, None, 'heat.jpg', 'image/jpeg', None, None)

        xray.prediction = predict
        xray.heatmap = heat_file
        xray.save()

    context = {
        'photo': xray.photo,
        'predict2': xray.prediction,
        'heatmap' : xray.heatmap,
        # 'predict1': predict1,
        # 'predict3': predict3,
        'created_at': xray.created_at,
        # 작성 날짜
        # 유저
    }

    return render(request, 'result.html', context)

def model(request):

    return render(request, 'model.html')
