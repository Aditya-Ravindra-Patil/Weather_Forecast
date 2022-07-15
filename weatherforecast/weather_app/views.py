
from datetime import datetime
from multiprocessing import context
from xmlrpc.client import _datetime
from django.shortcuts import redirect, render
import requests
import datetime

# Create your views here.

def home(request):
    #if request.method == "POST":
    city=request.GET.get('city',"Kolhapur")
    #city="Kolhapur"
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4ff9ebce3b1cb8d7d0e605a4aab56b5f'
    data=requests.get(url).json()
    datadoc={
        'location':data['name'], 
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'k_temprature':data['main']['temp'],
        'c_temprature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description':data['weather'][0]['description'],
        'day':datetime.date.today()
        
        
    }
    
    context={
        'data':datadoc
        
    }
    
        
    return render(request,'home.html', context)