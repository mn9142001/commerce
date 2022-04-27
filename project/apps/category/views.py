from django.shortcuts import render
from category.models import Category
# Create your views here.
def HomeView(request):

    return render(request, 'home/home.html', {'cats':Category.objects.all()})