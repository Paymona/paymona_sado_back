from django.http.response import HttpResponse
from django.shortcuts import redirect
from authorization.models import User
from home.controllers.assess import Assess
from home.models import Record
from django.shortcuts import render
from mutagen.mp3 import MP3


def audio_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return {'hours': round(hours), 'mins': round(mins), 'seconds': round(seconds)}


def MainController(request):
    if 'user_id' not in request.session:
        return redirect('/auth/login')
    
    try:
        user_query = User.objects.get(id=request.session.get('user_id'))
    except:
        request.session.pop('user_id')
        return redirect('/auth/login')

    record_query = Record.objects.all()

    data = {
        'all_records': record_query.count(),
        'recorded_hours': 0,
        'assessed_hours' : 0
    }

    temp_durations = 0
    for i in record_query:
        temp_durations += MP3(i._file).info.length

    temp_durations = round(temp_durations)

    if temp_durations < 60:
        data['recorded_hours'] = audio_duration(temp_durations).get('seconds')

    elif temp_durations > 60 and temp_durations < 3600:

        data['recorded_hours'] = audio_duration(temp_durations).get('mins')

    else:
        data['recorded_hours'] = audio_duration(temp_durations).get('hours')

    audio_duration(temp_durations)
    

    assess_query = Assess.objects.all()

    ass_duration = 0
    for i in assess_query:
        ass_duration += MP3(i._file).info.length
    
    ass_duration = round(ass_duration)


    if ass_duration < 60:
        data['assessed_hours'] = audio_duration(ass_duration).get('seconds')

    elif ass_duration > 60 and ass_duration < 3600:

        data['assessed_hours'] = audio_duration(ass_duration).get('mins')

    else:
        data['assessed_hours'] = audio_duration(ass_duration).get('hours')

    audio_duration(ass_duration)

    #return render(request, 'main.html', {"data" : data})
