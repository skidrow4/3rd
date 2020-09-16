from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목")  #  모델의 길이와 맞춘다..
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")
    #tags = forms.CharField(
    #    required=False, label="태그")
# 검증은 필요 없다. 기본적으로 들어 가있는게 값이 있는지 없는지 확인해 주었다 ??????

# 아래는 참고적으로 붙여 놓은것, 현재 프로그램이랑 상관 없음.....
class LoginForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },  #  required의 값을 바꾼다......기존 This Field is required라고 보면 된다.
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")
    # label 값을 사용하면 브라우저에서 사용이 된다

    def clean(self):  # clean() 함수가 원래 있는듯 ????......
        cleaned_data = super().clean()  
        # 기존에 만들어 져 있는 clean()함수를 사용하며, 
        # super() 즉 클래스의 forms.Form의 clean()함수를 먼저  호출한다 
        # 만약 값(데이타)가 없다면 여기서 실패처리가 되어서 나간다.
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:  # 값이 있을때 
            # 현재여기서 세션 처리 하지 않는다. 즉 검증만 하면 된다.
            fcuser = Fcuser.objects.get(username=username)
            
            if not check_password(password, fcuser.password):  # 값이 틀릴때
                # 앞 post입력받은값, 뒤는 모델의 값
                self.add_error('password', '비밀번호를 틀렸습니다')  # add_erro()함수가 있다
                # 특정 필드에다가 에러를 넣는 함수이다
            else:  #  정상적으로 비밀번호가 맞을때 
                self.user_id = fcuser.id  # views.py의 세션 처리 때문에 있다
