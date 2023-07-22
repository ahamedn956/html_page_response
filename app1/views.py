from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def naruto(request):
    return render(request,'naruto.html')
