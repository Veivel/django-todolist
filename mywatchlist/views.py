from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from mywatchlist.models import MyWatchlist

def show_html(request):
    list_watchlist = MyWatchlist.objects.all()
    context = {
        'list_watchlist': list_watchlist,
        'title': 'Tugas 3 PBP-D',
        'num_balance': len(list_watchlist.filter(watched=True)) - len(list_watchlist.filter(watched=False))
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")