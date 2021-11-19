from django.shortcuts import redirect
from authorization.models import User
from home.models import Record, Text
from django.shortcuts import render
from random import random
from mutagen.mp3 import MP3



def Record(request):
    if 'user_id' not in request.session:
        return redirect('/auth/login')
    if request.method == 'GET':
        return render(request, 'h.html')

    try:
        user_query = User.objects.get(id=request.session.get('user_id'))
    except:
        request.session.pop('user_id')
        return redirect('/auth/login')

    number_of_texts = Text.objects.count()
    random_index = int(random.random()*number_of_texts)+1
    random_text = Text.get(id = random_index)
    
    _record = request.FILES['record']
    temp_duration = round(MP3(_record).info.length)

    newrecord = Record(_file = _record, text = random_index, author = user_query.id, duration = temp_duration)
    newrecord.save()

    return render(request, 'main.html', {'random_text' : random_text})