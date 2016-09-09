from django.shortcuts import render
from django.http import HttpResponse
import os,re
from .models import Greeting,User,Movie,Rating

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    #return HttpResponse(os.listdir("/home/avais/Desktop/recommend-movies/recommend-movies/app/"))
    run_once()

    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def run_once():
    os.chdir("/home/avais/Desktop/recommend-movies/recommend-movies/app/")
    '''f = open("u.user", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 5)
        if len(e) == 5:
            if e[4] > 0:
                User.objects.get_or_create(userid=e[0], age=e[1], sex=e[2], occupation=e[3], zipcode=e[4])
    f.close()
    f = open("u.item", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 24)
        if len(e) == 24:
            Movie.objects.create(movieid=e[0], title=e[1], date=e[2], viddate=e[3], url=e[4], unknown=e[5], action=e[6], adventure=e[7], animation=e[8],
            childrens=e[9], comedy=e[10], crime=e[11], documentary=e[12], drama=e[13], fantasy=e[14], film_noir=e[15], 
            horror=e[16], musical=e[17], mystery=e[18], romance=e[19], sci_fi=e[20], thriller=e[21], \
            war=e[22], western=e[23])
    f.close()'''
    f = open("u.base", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for x in range(0,250):
        entry = entries[x]
        e = entry.split('\t', 4)
        if len(e) == 4:
            Rating.objects.create(userid=e[0], movieid=e[1], rating=e[2], time=e[3])
    f.close()