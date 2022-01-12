from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

# def log(request):
#     return render(request,'login.html')

def login(request):
    return render(request,'login.html')