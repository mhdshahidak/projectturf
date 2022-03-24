from django.shortcuts import redirect, render

from app.models import Customer
from owners.models import Turf

# Create your views here.
def home(request):
    turfs = Turf.objects.all()
    return render(request,'home.html',{'turfs':turfs,})


def login(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_exists = Customer.objects.filter(email=username,password=password)

        if user_exists:
            user_data = Customer.objects.get(email=username,password=password)
            request.session['customer'] = user_data.customer_id
            return redirect('app:userhome')
        else:
            msg = "username or password incorrect"
            return render(request,'login.html',{'msg':msg, })

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

