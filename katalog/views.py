from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    
    catalog = CatalogItem.objects.all()
    context = {
        'list_katalog': catalog,
        'nama': 'Givarrel Veivel Pattiwael',
        'npm': '2106640341'
    }
    
    return render(request, 'katalog.html', context)
