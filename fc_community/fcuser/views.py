from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.

#def register(request):
#    return render(request, 'register.html')    #  하위 폴더 가 있다면  forder1/forder2/register.html  

def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home! views.py에서 글자로 테스트')
    # return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):  # 로그인 했을때 
        del(request.session['user'])  # 세션 user를 삭제 한다.

    return redirect('/')


def login(request):
    print(dir(request))
    print(dir(request.session))
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력 해야 합니다.'
        else:
            fcuser = Fcuser.objects.get(username = username)   # username 쿼리해서 가져온 객체
            # username 앞은 모델안에서 속성 변수이고, /  뒷꺼는 POST가져온 변수값
            if check_password(password, fcuser.password):
                # check_password 함수....POST가져온 password , 모델에서 가져온 fcuser.password
                # 비밀번호가 일치, 로그인 처리를!
                # 세션!
                # 리다이렉트 홈, 로그인후 갈 페이지
                #print('---------1111',password, fcuser.password)
                request.session['user'] = fcuser.id
                print(request.session['user'])
                print(fcuser.id)
                print(dir(request.session.keys()))
                print(dir(request.session.values()))
                return redirect('/')  # '/' 홈 표현, 예: return redirect('http://naver.com')
            else:  #  비밀번호가 불일치
                print('---------2222',password, fcuser.password)
                res_data['error'] = '비밀번호가 틀렸읍니다.'
        return render(request, 'login.html', res_data)
    
def register(request):
    if request.method == 'GET':                    # url로 들어 올때
        return render(request, 'register.html')
    elif request.method == 'POST':                 # register.hmtl 의 등록 버턴 클릭후 다시 들어 올때 
        username = request.POST.get('username', None)  # form 데이타로 다시 돌어 올때이다
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)  # 원래는 POST['username'] 딕셔너리 기본형이다
        re_password = request.POST.get('re-password', None)  # 만약 키가 없으면 에러 난다. get으로 바꾼다
                         # key 값을 없을때 기본값 지정한다. None은 거짓의 의미이다 == '' == 0  써도 된다

        res_data = {}   # 화면에 보낼 메세지 데이타 변수, 딕셔너리형태

        if not (username and useremail and password and re_password):  # 빈 문자열이 즉 공백이 올때나 값이 없을때
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:                                  # 패스워드와 확인패스워드가 틀릴때
            res_data['error'] = '비밀번호가 다릅니다.'  # 딕셔너리 데이타 생성
            # return HttpResponse('비밀번호가 다릅니다.')
        else:                                                          # 정상적으로 돌아 갈때
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                # password=password
                password=make_password(password)  # 패스워드 암호화 하여 db에 들어 간다.
            )

            fcuser.save()

        return render(request, 'register.html', res_data)  #  html에서 받아주는 변수문법이 있어야 한다..
        # [error : '비밀번호가 다릅니다'] 있는것과 같다....... 갯수가 많을수도 있다...


