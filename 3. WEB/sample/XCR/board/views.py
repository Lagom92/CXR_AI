from django.http import request
from django.shortcuts import redirect, render
from .models import Xray

# 메인 
def home(request):

    return render(request, 'home.html')


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

    # Predict 추가 예정
    predict = ""

    context = {
        'title': xray.title,
        'photo': xray.photo,
        'predict': predict
    }

    return render(request, 'result.html', context)

