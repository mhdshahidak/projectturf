from django.shortcuts import render

from owners.models import Owners

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


      if password == cpassword:
          new_owner = Owners(owner_name=name,email=email,court_name=court_name, sports_type=sport_type, phone_no=contactnumber, booking_no=booknumber, location=location,password=password)
          new_owner.save()
          msg = "Registerd successfully"
      else:
          msg = "Incorrect password "

    return render(request,'register.html', {'msg':msg, })

def owelogin(request):
    return render(request,'owelogin.html')

def booking(request):
    return render(request,'booking.html')