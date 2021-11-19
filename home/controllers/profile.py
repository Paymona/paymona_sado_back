from datetime import date, datetime
from django.shortcuts import redirect
from authorization.models import User
from home.models import Record, Assess
from django.shortcuts import render
from mutagen.mp3 import MP3

def ProfileController(request):
    if 'user_id' not in request.session:
        return redirect('/auth/login')
    
    try:
        user_query = User.objects.get(id=request.session.get('user_id'))
    except:
        request.session.pop('user_id')
        return redirect('/auth/login')

    

    record_query = Record.objects.filter(
        author = user_query.id, 
        date__range=(request.session['timestamp_login'], datetime.now()
    ))

    temp_durations = 0
    for i in record_query:
        temp_durations += MP3(i._file).info.length

    temp_durations = round(temp_durations)


    assess_query = Assess.objects.filter(
        who = user_query.id, 
        date__range=(request.session['timestamp_login'], datetime.now()
    ))

    ass_duration = 0
    for i in assess_query:
        ass_duration += MP3(i._file).info.length
    
    ass_duration = round(ass_duration)

    data = {
        'name' : user_query.username,
        'email' : user_query.email,
        'age' : user_query.age,
        'gender' : user_query.gender,
        'city' : user_query.city,
        'dialect' : user_query.dialect,
        'recorded' : temp_durations,
        'assessed' : ass_duration
    }
    

    return render(request, 'huyznaet.html', {'data' : data})