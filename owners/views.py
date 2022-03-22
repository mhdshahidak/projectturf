from django.shortcuts import render

# Create your views here.
def register(request):
    msg = ""
    # if request.method == 'POST':

    return render(request,'register.html')

def owelogin(request):
    return render(request,'owelogin.html')

def booking(request):
    return render(request,'booking.html')