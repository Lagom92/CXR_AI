from django.http import request
from django.shortcuts import render, redirect
from tensorflow.python.eager.context import context
from .models import Xray, CoughAudio, MultiData
from .apps import BoardsConfig
from boards.myPredicts import make_wav2img, predict_multiInput

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
        prediction = BoardsConfig.predict_CXR(xray.photo.path)
        xray.prediction = prediction
        xray.save()
    title = xray.photo.url.split('/')[-1]
    return render(request, 'result.html', {'xray': xray, 'title': title})

# 오디오
def audiotest(request):
    if request.method == 'POST':
        cough = CoughAudio.objects.create(
            audio = request.FILES['audio'],
            )
        return redirect('audioresult')

    else:
        return render(request, 'audiotest.html')


# 오디오 확인
def audioresult(request):
    cough = CoughAudio.objects.last()
    if not cough.prediction:
        audio_path = cough.audio.path
        image_path = make_wav2img(audio_path)
        prediction = BoardsConfig.predict_audio(image_path)
        cough.mel = image_path[8:]
        cough.prediction = prediction
        cough.save()
    return render(request, 'audioresult.html', {'cough': cough})


# 멀티
def multitest(request):
    if request.method == 'POST':
        multi = MultiData.objects.create(
            photo = request.FILES['photo'],
            audio = request.FILES['audio'],
            )
        return redirect('multiresult')

    else:
        return render(request, 'multitest.html')


# 멀티 확인
def multiresult(request):
    multi = MultiData.objects.last()
    if not multi.prediction:
        audio_mel_path = make_wav2img(multi.audio.path)
        prediction = predict_multiInput(multi.photo.path, audio_mel_path)
        multi.mel = audio_mel_path[8:]
        multi.prediction = prediction
        multi.save()

    return render(request, 'multiresult.html', {'multi': multi})




# ------------------------------------------------------------------------------
def model(request):

    return render(request, 'model.html')



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



def detail(request, user_id, id):
    if request.user.id != user_id:
        return redirect('main')
    else:
        xray = Xray.objects.get(id=id)
        context = {
            'xray': xray
        }

    return render(request, 'detail.html', context)



def visualization(request):

    return render(request, 'visualization.html')


def delete(request, user_id, id):
    if request.user.id != user_id:
        return redirect('main')
    else:
        xray = Xray.objects.get(id=id)
        xray.delete()
        return redirect('main')


def member(request):

    return render(request, 'member.html')

