from django.shortcuts import redirect, render

from adminapp.models import AdminLog
from owners.models import Owners, Turf

# Create your views here.

def login(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        admin_exists = AdminLog.objects.filter(username=username,password=password)

        if admin_exists:
            user_data = AdminLog.objects.get(username=username,password=password)
            request.session['admin'] = user_data.id
            return redirect('adminapp:adminhome')
        else:
            msg = "username or password incorrect"
            return render(request,'login.html',{'msg':msg, })

    return render(request,'login.html')

def admin_home(request):
    turf = Owners.objects.filter(status='requested')
    return render(request,'admin_home.html',{'turf':turf,})

def approve(request,id):
    status = "approved"
    Owners.objects.filter(owner_id=id).update(status=status)
    return redirect('adminapp:adminhome')

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('adminapp:adminlogin')

def details(request):
    owners_dts = Owners.objects.all()
    return render(request,'details.html',{'owner':owners_dts,})

def Deactivate(request,id):
    status = "DeActivate"
    Owners.objects.filter(owner_id=id).update(status=status)
    return redirect('adminapp:details')

def delete(request):
    pass

