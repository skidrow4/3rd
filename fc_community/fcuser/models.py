from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')   #  EmailField 메일 검증을 한다 @ 있나 없나.
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')
                                           
    # dttm  datetime 약자,  auto_now_add=True  입력시 자동 현재 시간 입력
    # verbose_name 나중에 한글명으로 보일수 있다 (브라우저에서 admin 들어 가면 보임 )

    def __str__(self):  # 클라스의 오브젝트를 문자열 반환시 사용한다. 이것 없으면 Fcuser object로 나온다..함수명 object로 나온다
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'     # 테이블 명  없어도 상관 없으나  나중에 관리상 필요
        verbose_name = '패스트캠퍼스 사용자'    # Fcuser 이름 명칭 설정 / 복수형과 같은 이름 사용해도 큰지장 없다
        verbose_name_plural = '패스트캠퍼스 사용자'  # Fcusers 복수형 s가 있는 이름명칭  1번

