from django.shortcuts import render
from .models import Report
from .forms import RequestReport, VisitorReport
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

from bluebiulding.reports.api import cryptoAPI


def index(request):
    # If the user is login
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RequestReport(request.POST)
            if form.is_valid():
                fs = form.save(commit=False)
                if Report.objects.filter(cryptocurrency=fs.cryptocurrency, name=request.user):
                    return HttpResponseRedirect(reverse('accounts:dashboard')) 

                else:
                    fs.name = request.user
                    fs.save()
                    context = {
                    'form': form,
                    }

                    return HttpResponseRedirect(reverse('reports:exhibition'))
                    
        else:
            form = RequestReport()
            context = {
                'form': form,
            }
            
            return render(request, 'reports/index.html', context=context)
    else:
        # If the the user is a visitor
        if request.method == 'POST':
            form = VisitorReport(request.POST)
            if form.is_valid():
                data = request.POST
                request.session['data'] = data
                context = {
                'form': form,
                }

                return HttpResponseRedirect(reverse('reports:exhibition'))   
        else:
            form = VisitorReport()
            context = {
                'form': form,
            }
            
            return render(request, 'reports/index.html', context=context)


def exhibition(request):
    if request.user.is_authenticated:
        data = Report.objects.latest('id')
        your_name = str(data.name)
        cryptocurrency = str(data.cryptocurrency)

        context = cryptoAPI(your_name, cryptocurrency)

        return render(request, 'reports/exhibition.html', context)
    else:
        data = request.session.get('data')
        your_name = data['name']
        cryptocurrency = data['cryptocurrency']
        
        context = cryptoAPI(your_name, cryptocurrency)

        return render(request, 'reports/exhibition.html', context)






















'''
from django.shortcuts import get_object_or_404
import os

def index(request):
    reports = Report.objects.all()
    template_name = 'reports/index.html'
    context = {}
    if request.method == 'POST':
        form = RequestReport(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = RequestReport()
            #form.save()
            return HttpResponseRedirect(reverse('reports:exhibitionDB'))
    
    reports = Report.objects.all()
    template_name = 'reports/index.html'
    context = {}

    return render(request, 'reports/index.html', context=context)


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
def exhibition(request):
    if request.user.is_authenticated():
    seu_nome = request.user.username


    if request.user.is_authenticated:
        data = Report.objects.latest('id')
        seu_nome = str(data.name)
        cryptocurrency = str(data.cryptocurrency)
    else:
        data = request.session.get('data')
        seu_nome = data['name']
        cryptocurrency = data['cryptocurrency']
    
    print(data)
    print(seu_nome)
    print(cryptocurrency)

    # API to collect cryptocurrency financial information
    urlQuote = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    # API to collect basic cryptocurrency information.
    urlInfo = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

    parameters = {
        'symbol' : cryptocurrency,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '3cb96add-56a5-43d6-8fb3-1c3a2284e462',
    }

    session = Session()
    session.headers.update(headers)


    #API Cryptocurrency Quotes Latest
    try:
        response1 = session.get(urlQuote, params=parameters)
        data1 = json.loads(response1.text)
        
        price = str(data1['data'][cryptocurrency]['quote']['USD']['price'])
        volume_24h = str(data1['data'][cryptocurrency]['quote']['USD']['volume_24h'])
        percent_change_1h = str(data1['data'][cryptocurrency]['quote']['USD']['percent_change_1h'])
        percent_change_24h = str(data1['data'][cryptocurrency]['quote']['USD']['percent_change_24h'])
        percent_change_7d = str(data1['data'][cryptocurrency]['quote']['USD']['percent_change_7d'])
        market_cap = str(data1['data'][cryptocurrency]['quote']['USD']['market_cap'])

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
            

    #API Cryptocurrency Info
    try:
        response = session.get(urlInfo, params=parameters)
        data = json.loads(response.text)

        website = data['data'][cryptocurrency]['urls']['website'][0]
        technical_doc = data['data'][cryptocurrency]['urls']['technical_doc'][0]
        id=data['data'][cryptocurrency]['id']
        name=data['data'][cryptocurrency]['name']
        symbol=data['data'][cryptocurrency]['symbol']
        category=data['data'][cryptocurrency]['category']
        slug=data['data'][cryptocurrency]['slug']
        logo=data['data'][cryptocurrency]['logo']
        description=data['data'][cryptocurrency]['description']
        date_added=data['data'][cryptocurrency]['date_added']
        notice=data['data'][cryptocurrency]['notice']
        tags=data['data'][cryptocurrency]['tags']
        explorer = data['data'][cryptocurrency]['urls']['explorer']
        
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    context = {
        'seu_nome' : seu_nome,
        'website' : website,
        'technical_doc' : technical_doc,
        'id' : id,
        'name' : name,
        'symbol' : symbol,
        'category' : category,
        'slug' : slug,
        'logo' : logo,
        'description' : description,
        'date_added' : date_added,
        'notice' : notice,
        'tags' : tags,
        'price' : price,
        'volume_24h' : volume_24h,
        'percent_change_1h' : percent_change_1h,
        'percent_change_24h' : percent_change_24h,
        'percent_change_7d' : percent_change_7d,
        'market_cap' : market_cap,
        'explorer' : explorer

    }
    return render(request, 'reports/exhibition.html', context)
'''