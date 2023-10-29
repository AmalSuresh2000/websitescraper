from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from websitescraper_app.models import Links


# Create your views here.

def home (request):
    urls = requests.get("https://www.google.com/")
    soup = BeautifulSoup (urls.text,'html.parser')
    address = []
    for links in soup.find_all('a'):
        li_address=links.get('href')
        li_name=links.string
        Links.objects.create(address=li_address,stringname=li_name)
        data_values=Links.objects.all()
    return render(request,'home.html',{'data_values':data_values})