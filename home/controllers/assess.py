from django.shortcuts import redirect
from authorization.models import User
from home.models import Record
from django.shortcuts import render
from random import random

def Assess(request):
    if 'user_id' not in request.session:
        return redirect('/auth/login')
    
    try:
        user_query = User.objects.get(id=request.session.get('user_id'))
    except:
        request.session.pop('user_id')
        return redirect('/auth/login')

    number_of_records = Record.objects.count()
    random_index = int(random.random()*number_of_records)+1
    random_record = Record.get(id = random_index)

    _text = random_record.text

    data = {
        'record' : random_record,
        'text' : _text
    }

    like = request.POST.get('like', '')
    dislike = request.POST.get('dislike', '')

    if like == '' and dislike != '':
        random_record.dislikes += 1
    elif like != '' and dislike == '':
        random_record.likes +=1
    
    newassess = Assess(record = random_index, who = user_query.id)
    newassess.save()

    return render(request, 'herznaet.html', {'data' : data})