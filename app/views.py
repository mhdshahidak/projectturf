from django.shortcuts import render

from app.models import Customer

# Create your views here.
def home(request):
    return render(request,'home.html')

# def log(request):
#     return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        genter = request.POST['genter']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            email_exist = Customer.objects.filter(email=email).exists()
            if not email_exist:
                new_customer = Customer(name=name, email=email, phone=phone, genter=genter, password=password)
                new_customer.save()
                msg = "Registerd successfully"
            else:
                msg = "Email already exists"
        else:
            msg = "incorrect password"
    return render(request,'signup.html',{'msg':msg, })


def master(request):
    return render(request, 'master.html')

