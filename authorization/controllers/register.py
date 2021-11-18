from django.shortcuts import redirect, render
from ..models import User

def RegisterController(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    _username = request.POST.get('username', '')
    _email = request.POST.get('email', '')
    _password = request.POST.get('password', '')


    if _username =='' or _email == '' or _password == '':
        return  render(request, 'register.html', {"error" : "Empty Field"})

    user = User(username = _username, email = _email, password = _password)
    user.save()
    
    return redirect('/auth/login')
