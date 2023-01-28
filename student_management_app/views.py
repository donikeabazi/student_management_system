from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDemoPage(request):
    if request.user.is_authenticated:
        return render(request, "demo.html")
    return render(request, "login_page.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method No Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type=="2":
                return HttpResponse("Staff Login"+str(user.user_type))
            else:
                return HttpResponse("Student Login"+str(user.user_type))   
        else:
            messages.error(request, "Invalid Login Details") 
            return HttpResponseRedirect("/")
        
def GetUserDetails(request):
    if request.user!=None:
        return render("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return render("Please Login First")
    
def logout_user(request):
    logout(request)
    return redirect('/')
    
        
        
    
        
            
         