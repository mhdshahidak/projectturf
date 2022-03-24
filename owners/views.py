from django.shortcuts import redirect, render

from owners.models import Owners, Turf

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

def booking(request):
    return render(request,'booking.html')

def turfhome(request):
    try:

        turf = Owners.objects.get(owner_id=request.session['owner'])


        pics = Turf.objects.get(owner_id=request.session['owner'])

        return render(request, 'turf_home.html',{'turf':turf,'pics':pics})  
    except Exception:
        return render(request, 'turf_home.html',{'turf':turf,})  


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

def logout(request):
    del request.session['owner']
    request.session.flush()
    return redirect('owners:owelogin')