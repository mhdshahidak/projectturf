from django.shortcuts import redirect


def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'customer' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('app:loginpage')
            
    return wrap


def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if 'admin' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('adminapp:adminlogin')
            
    return wrap


def auth_owner(func):
    def wrap(request, *args, **kwargs):
        if 'owner' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('owners:owelogin')
            
    return wrap