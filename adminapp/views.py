from django.shortcuts import redirect, render

from adminapp.models import AdminLog
from owners.models import Owners, Turf
from turf.decorators import auth_admin
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def login(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        admin_exists = AdminLog.objects.filter(
            username=username, password=password)

        if admin_exists:
            user_data = AdminLog.objects.get(
                username=username, password=password)
            request.session['admin'] = user_data.id
            return redirect('adminapp:adminhome')
        else:
            msg = "username or password incorrect"
            return render(request, 'login.html', {'msg': msg, })

    return render(request, 'login.html')


@auth_admin
def admin_home(request):
    turf = Owners.objects.filter(status='requested')
    return render(request, 'admin_home.html', {'turf': turf, })


@auth_admin
def approve(request, id):
    status = "approved"
    Owners.objects.filter(owner_id=id).update(status=status)
    owner = Owners.objects.get(owner_id=id)
    send_mail("PLAY MANIA", " You get approved by Admin you can now login to your profile page ",settings.EMAIL_HOST_USER, [str(owner.email)])
                    
            
    return redirect('adminapp:adminhome')


@auth_admin
def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('adminapp:adminlogin')


@auth_admin
def details(request):
    owners_dts = Owners.objects.all()
    return render(request, 'details.html', {'owner': owners_dts, })


@auth_admin
def Deactivate(request, id):
    status = "DeActivate"
    Owners.objects.filter(owner_id=id).update(status=status)
    return redirect('adminapp:details')


@auth_admin
def delete(request, id):
    Owners.objects.get(owner_id=id).delete()
    return redirect('adminapp:details')
