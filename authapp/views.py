from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import random

USER = {
    "username": "admin",
    "password": "1234"
}

def login_view(request):
    if request.user.is_authenticated:
        return redirect('generate_code')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == USER["username"] and password == USER["password"]:
            request.session['logged_in'] = True
            return redirect('generate_code')
        else:
            return HttpResponse("ERROR", status=401)

    return render(request, "login.html")

def generate_code(request):
    if not request.session.get('logged_in'):
        return redirect('login')

    code = random.randint(1000, 9999)
    request.session.flush() 
    return HttpResponse(f"<h1>Code : {code}</h1>")
