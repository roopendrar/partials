from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trails(request):
    return HttpResponse("<h1>project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"app3/home.html")

def profile(request):
    name="rocky"
    return render(request,"app3/profile.html",{'name':name})