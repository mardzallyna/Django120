from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Home view
def home(request):
   return render(request, 'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')  # Redirect to the dashboard or home page after login
        else:
            return HttpResponse("Invalid credentials", status=401)

    return render(request, 'authentication/login.html')
