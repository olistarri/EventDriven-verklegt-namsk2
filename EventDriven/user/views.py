from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'user/loginpage.html')

@login_required
def profile(request):
    return render(request, 'user/userprofile.html')
