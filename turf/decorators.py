from django.shortcuts import redirect


def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'customer' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('app:loginpage')
            
    return wrap
