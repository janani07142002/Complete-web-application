from django.shortcuts import render, redirect
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('/')
    return render(request, 'add.html')