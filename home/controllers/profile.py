from django.shortcuts import redirect
from authorization.models import User
from home.models import Record
from django.shortcuts import render

def ProfileController(request):
    if 'user_id' not in request.session:
        return redirect('/auth/login')
    
    try:
        user_query = User.objects.get(id=request.session.get('user_id'))
    except:
        request.session.pop('user_id')
        return redirect('/auth/login')

    record_query = Record.objects.get(user_query.id)

    data = {
        'name' : user_query.username,
        'email' : user_query.email,
        'age' : user_query.age,
        'gender' : user_query.gender,
        'city' : user_query.city,
        'dialect' : user_query.dialect
    }
    

