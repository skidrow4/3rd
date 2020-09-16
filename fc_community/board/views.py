from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm

# Create your views here.


def board_detail(request, pk):
    # board = Board.objects.get(pk=pk)
    try:  # 예외 처리,  직접 url에서 숫자를 넣어서 직접들어 올때의  없는글 찾을때....
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'):  #  예외처리 : 리퀘스트 세션에 유저가 없으면 
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')  #  세션에서 user 정보 가져오기....
            fcuser = Fcuser.objects.get(pk=user_id)

            #tags = form.cleaned_data['tags'].split(',')
            # 보드생성
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')  #  모든글을 가져오는데 '-'의뜻 역순 (최신글 부터)
    page = int(request.GET.get('p', 1))  #  페이지 번호 받는다.. 지정없이 url페이지로 들어 온다면 1페이지가 기본으로 보인다
    paginator = Paginator(all_boards, 2)  #  한페이지에 게시글 갯수 지정.....

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
