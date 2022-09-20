from unittest import TextTestRunner
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from mywatchlist.models import MyWatchlist

# Create your views here.
# def CustomParser(data):
#     ''' Source: https://stackoverflow.com/questions/43668533/access-a-json-column-with-pandas '''
#     import json
#     j1 = json.loads(data)
#     return j1

# def get_watch_balance():    
#     ''' Returns an integer, number of movies watched - number of movies not watched.
#     Positive means more movies watched, negative means more movies not watched.'''
    
#     df = pd.read_json('mywatchlist/fixtures/initial_watchlist_data.json')
#     df = pd.json_normalize(df['fields'])
#     true_num = df[df['watched'] == True].shape[0]
#     false_num = df[df['watched'] == False].shape[0]
    
#     return true_num - false_num

def show_html(request):
    list_watchlist = MyWatchlist.objects.all()
    context = {
        'list_watchlist': list_watchlist,
        'title': 'Tugas 3 PBP-D',
        'num_balance': len(list_watchlist.filter(watched=True)) - len(list_watchlist.filter(watched=True))
    }
    
    return render(request, 'watchlist.html', context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")