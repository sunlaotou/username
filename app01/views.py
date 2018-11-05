from django.shortcuts import render ,HttpResponse ,redirect
from  django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        print (user ,pwd)
        user = auth.authenticate(username=user,password=pwd)
        if user:
            auth.login(request, user) # request.user:当前登录对象
            net_url= request.GET.get("next","/index/") #查找 next后面的url ,找不到返回、index函数
            return  redirect(net_url)

    return  render(request ,"login.html")
@login_required
def index(request):
    # print("request.user:",request.user.username)
    # print("request.user:",request.user.id)
    # print("request.user:",request.user.is_anonymous)
    # username = request.user.username
    # if  not username:
    #     return  redirect("/login/")
    return render(request,"index.html" ,locals())
def logout(request):
    auth.logout(request)
    return redirect("/login/")
def reg(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        User.objects.create_superuser(username=user,password=pwd,email=email)
        return redirect("/login/")

    return  render(request,"reg.html")