from django.http import request
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.decorators import login_required
from io import BytesIO

from tensorflow.python.eager.context import context
from .models import Xray
from .ml.predict import inception_resnt_predict_CXR_and_heatmap , prediction, diseasePredict

def main(request):

    return render(request, 'main.html')

# # 이미지 요청 
def test(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            xray = Xray.objects.create(
                photo = request.FILES['image'],
                user = request.user
            )
        else:
            xray = Xray.objects.create(
                photo = request.FILES['image'],
            )
        return redirect('result')

    else:
        return render(request, 'test.html')


# 이미지 확인
def result(request):
    xray = Xray.objects.last()

    if not xray.prediction:
        predict, heatmap, plot = inception_resnt_predict_CXR_and_heatmap(xray.photo.path)
        heatmap_io = BytesIO()
        heatmap.save(heatmap_io, format='jpeg')
        heat_file = InMemoryUploadedFile(heatmap_io, None, 'heat.jpg', 'image/jpeg', None, None)

        plot_io = BytesIO()
        plot.save(plot_io, format='jpeg')
        plot_file = InMemoryUploadedFile(plot_io, None, 'plot.jpg', 'image/jpeg', None, None)

        xray.prediction = predict
        xray.heatmap = heat_file
        xray.plot = plot_file
        xray.save()

    context = {
        'photo': xray.photo,
        'predict2': xray.prediction,
        'heatmap' : xray.heatmap,
        'plot' : xray.plot,
        'created_at': xray.created_at,
    }

    return render(request, 'result.html', context)

def model(request):

    return render(request, 'model.html')

@login_required
def history(request, user_id):
    if request.user.id != user_id:
        return redirect('main')
    else:
        xrays = Xray.objects.filter(user_id=user_id)
        context = {
            'user': request.user,
            'xrays': xrays
        }

    return render(request, 'history.html', context)

@login_required
def detail(request, user_id, id):
    if request.user.id != user_id:
        return redirect('main')
    else:
        xray = Xray.objects.get(id=id)
        context = {
            'xray': xray
        }

    return render(request, 'detail.html', context)