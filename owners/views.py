import datetime 

from django.shortcuts import redirect, render
from app.models import Customer

from owners.models import Booking, Owners, Turf
from turf.decorators import auth_customer, auth_owner

# Create your views here.
def register(request):
    msg = ""
    if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      court_name = request.POST['courtname']
      sport_type = request.POST['sportstype']
      contactnumber = request.POST['contactnumber']
      booknumber = request.POST['bookingnumber']
      location = request.POST['location']
      password = request.POST['password']
      cpassword = request.POST['cpassword']

      email_exists = Owners.objects.filter(email=email).exists()
      

      if password == cpassword:
          if not email_exists:
              new_owner = Owners(owner_name=name,email=email,court_name=court_name, sports_type=sport_type, phone_no=contactnumber, booking_no=booknumber, location=location,password=password)
              new_owner.save()
              msg = "Registerd successfully"
          else:
              msg = "email already exists"     
      else:
          msg = "Incorrect password "

    return render(request,'register.html', {'msg':msg, })

def owelogin(request):
    msg = ""
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            owner_data = Owners.objects.get(email=username, password=password)

            if owner_data.status=='approved':
                request.session['owner'] = owner_data.owner_id
                return redirect('owners:turfhome')
            else:
                msg = "Account Not Approved"
                return render(request,'owelogin.html', {'msg':msg, })

        except :
           
            msg = "Username or Password incorrect"
            return render(request,'owelogin.html', {'msg':msg, })
        
    return render(request,'owelogin.html')

@auth_customer
def booking(request, id):
    wrking_date=[]
    turf = Turf.objects.get(id=id)
    current_date=datetime.date.today()
    for i in range(1,8):
        d=current_date+datetime.timedelta(days=i)
        wrking_date.append(d)
    return render(request,'booking.html',{'turf':turf,'wrking_date':wrking_date})

@auth_owner
def turfhome(request):
    try:

        turf = Owners.objects.get(owner_id=request.session['owner'])


        pics = Turf.objects.get(owner_id=request.session['owner'])

        return render(request, 'turf_home.html',{'turf':turf,'pics':pics})  
    except Exception:
        return render(request, 'turf_home.html',{'turf':turf,})  

@auth_owner
def update(request):
    msg = ""
    turf = Owners.objects.get(owner_id=request.session['owner'])

    if request.method == 'POST':
        proimage = request.FILES['proimg']
        cimg = request.FILES['cimg']
        fimg = request.FILES['fimg']
        simg = request.FILES['simg']
        timg = request.FILES['timg']

        owner_id = Owners.objects.get(owner_id=request.session['owner'])

        turf_dtls = Turf(owner_id=owner_id,profile_image=proimage,bg_image=cimg,first_image=fimg,second_image=simg,third_image=timg)
        turf_dtls.save()
        msg = "Updated successfully"
    
    return render(request,'update.html',{'msg':msg, 'turf':turf})

@auth_customer
def book(request, id):
    status = "Booked"
    time = request.GET['time']
    date = request.GET['dt']
    # date = date[2], date[1], date[0]

    turf = Turf.objects.get(id=id)
    customer = Customer.objects.get(customer_id=request.session['customer'])
    # print(type(date))
    if request.method == 'POST':
       
        time = request.POST['time']
        date = request.POST['date']

        turf_id = Turf.objects.get(id=id)
        customer_id = Customer.objects.get(customer_id=request.session['customer'])
        booking = Booking(turf_id=turf_id,user_id=customer_id,date=date,time=time,status=status)
        booking.save()
        return redirect('app:userhome')

    return render(request, 'book.html',{'turf':turf,'customer':customer,'date':date,'time':time})


     

@auth_owner
def logout(request):
    del request.session['owner']
    request.session.flush()
    return redirect('owners:owelogin')

@auth_customer
def clogout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('app:userhome')