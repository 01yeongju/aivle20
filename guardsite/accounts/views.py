from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("main"))
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect(reverse("main"))
            else:
                # print("로그인에 실패했습니다")
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        context = {"form": form}
        return render(request, "accounts/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))