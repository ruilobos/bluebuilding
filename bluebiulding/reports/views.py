from django.shortcuts import render, get_object_or_404
from .models import Report
from .forms import RequestReport
from django.http import HttpResponseRedirect
from django.urls import reverse

import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

# Create your views here.

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
            return HttpResponseRedirect(reverse('reports:exhibition'))

    else:
        form = RequestReport()
        context['form'] = form
        context['report'] = reports
        return render(request, template_name, context)

def exhibition(request):
    dados_relatorio = Report.objects.all()
    seu_nome = dados_relatorio['name']
    cryptocurrency = dados_relatorio['bitcoin']

    # API para coletar as informacoes financeiras da criptomoeda
    url1 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters1 = {
        'slug' : cryptocurrency,
    }
    headers1 = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '3cb96add-56a5-43d6-8fb3-1c3a2284e462',
    }

    session1 = Session()
    session1.headers.update(headers1)

    try:
        response1 = session1.get(url1, params=parameters1)
        data1 = json.loads(response1.text)
        price = str(data1['data']['1']['quote']['USD']['price'])
        volume_24h = str(data1['data']['1']['quote']['USD']['volume_24h'])
        percent_change_1h = str(data1['data']['1']['quote']['USD']['percent_change_1h'])
        percent_change_24h = str(data1['data']['1']['quote']['USD']['percent_change_24h'])
        percent_change_7d = str(data1['data']['1']['quote']['USD']['percent_change_7d'])
        market_cap = str(data1['data']['1']['quote']['USD']['market_cap'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
            

    # API para coletar as informacoes basicas da cryptomoeda.
    cripto_slug=cryptocurrency
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    parameters = {
        'slug': cripto_slug,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '3cb96add-56a5-43d6-8fb3-1c3a2284e462',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        website = data['data']['1']['urls']['website'][0]
        technical_doc = data['data']['1']['urls']['technical_doc'][0]
        id=data['data']['1']['id']
        name=data['data']['1']['name']
        symbol=data['data']['1']['symbol']
        category=data['data']['1']['category']
        slug=data['data']['1']['slug']
        logo=data['data']['1']['logo']
        description=data['data']['1']['description']
        date_added=data['data']['1']['date_added']
        notice=data['data']['1']['notice']
        tags=data['data']['1']['tags']
        explorer = data['data']['1']['urls']['explorer']
        
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