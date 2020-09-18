from django.http import request
from django.shortcuts import render, redirect
from .models import Xray
from .ml.predict import inception_resnt_predict_CXR_and_heatmap , prediction#,diseasePredict
# from .forms import UploadForm

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
        # redirect -- 시스템에 변화가 있을 때는 redirect를 사용.
        return redirect('result')
    else:
        return render(request, 'main.html')

# 이미지 확인
def result(request):
    # detect함수에서 생성한 Xray오브젝트는 데이터베이스에 
    # 계속 축적되므로 가장 마지막(최신)의 오브젝트를 가져와서 보여준다.
    xray = Xray.objects.last()
    predict, heatmap = inception_resnt_predict_CXR_and_heatmap(xray.photo.path)
    # 장고 모델파라미터에 heatmap이미지를 저장하기 위한 코드
    from io import BytesIO
    from django.core.files.uploadedfile import InMemoryUploadedFile

    heatmap_io = BytesIO()
    heatmap.save(heatmap_io, format='jpeg')
    # 장고의 requests.FILES type과 같게 만들어주는 모듈 
    heat_file = InMemoryUploadedFile(heatmap_io, None, 'heat.jpg', 'image/jpeg',
                                    None, None)
    # 모델의 파라미터에 이미지를 저장
    xray.heatmap = heat_file
    xray.save()
    # 제목, 원본이미지, 예측, 히트맵이미지를 html에 넘겨준다.

    #주연 테스트
    predict1 = prediction(xray.photo.path)

    context = {
        'title': xray.title,
        'photo': xray.photo,
        'predict1': predict1,
        'predict2': predict,
        'heatmap' : xray.heatmap
    }

    return render(request, 'result.html', context)