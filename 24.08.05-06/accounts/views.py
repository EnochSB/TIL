from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login #views에 작성할 login과 구분하기 위해 재명명
from django.contrib.auth import logout as auth_logout #views에 작성할 logout과 구분하기 위해 재명명
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

# 세션을 create
def login(request):
    #로그인 여부 확인
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)    #유저가 존재하는 검증하는 django 내장 모델폼. 검증만 할 뿐 세션과는 무관.
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())    #유저 정보를  세션에  생성 및 저장하는 django 내장함수
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# 세션을 delete. session data를 db에서 삭제, 클라이언트 쿠키에서도 sessionid를 삭제
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원 가입 후 자동 로그인
            # user = form.save()
            # auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)    # 세션정보 지우기, 탈퇴 후 로그아웃(반대로 하면 탈퇴가 안됨.)
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경시 로그아웃 방지, 새로운 password session data로 기존 session 업데이트
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)