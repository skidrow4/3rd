from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.

#def register(request):
#    return render(request, 'register.html')    #  하위 폴더 가 있다면  forder1/forder2/register.html  

def register(request):
    if request.method == 'GET':                    # url로 들어 올때
        return render(request, 'register.html')
    elif request.method == 'POST':                 # register.hmtl 의 등록 버턴 클릭후 다시 들어 올때 
        username = request.POST.get('username', None)  # form 데이타로 다시 돌어 올때이다
        password = request.POST.get('password', None)  # 원래는 POST['username'] 딕셔너리 기본형이다
        re_password = request.POST.get('re-password', None)  # 만약 키가 없으면 에러 난다. get으로 바꾼다
                         # key 값을 없을때 기본값 지정한다. None은 거짓의 의미이다 == '' == 0  써도 된다

        res_data = {}   # 화면에 보낼 메세지 데이타 변수, 딕셔너리형태

        if not (username and password and re_password):  # 빈 문자열이 즉 공백이 올때나 값이 없을때
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:                                  # 패스워드와 확인패스워드가 틀릴때
            res_data['error'] = '비밀번호가 다릅니다.'  # 딕셔너리 데이타 생성
            # return HttpResponse('비밀번호가 다릅니다.')
        else:                                                          # 정상적으로 돌아 갈때
            fcuser = Fcuser(
                username=username,
                # password=password
                password=make_password(password)  # 패스워드 암호화 하여 db에 들어 간다.
            )

            fcuser.save()

        return render(request, 'register.html', res_data)  #  html에서 받아주는 변수문법이 있어야 한다..
        # [error : '비밀번호가 다릅니다'] 있는것과 같다....... 갯수가 많을수도 있다...


