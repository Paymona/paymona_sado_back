from datetime import datetime
from django.shortcuts import redirect, render
from ..models import User

def LoginController(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    _email = request.POST.get('email', '')
    _password = request.POST.get('password', '')

    if _email == '' or _password == '':
        return  render(request, 'login.html', {"error" : "Empty Field"})
    
    try:
       user_query =  User.objects.get(email =_email)
    except:
        return render(request, 'login.html', {"error" : "Wrong Email or Password"})
    
    if user_query.password != _password:
        return render(request, 'login.html', {"error" : "Wrong Email or Password"})
    
    request.session['user_id'] = user_query.id
    request.session['timestamp_login'] = datetime.now()

    return redirect('/')