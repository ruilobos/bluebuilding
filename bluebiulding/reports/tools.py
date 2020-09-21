import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

def get_symbol():
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'1',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9484b998-5485-4933-b161-2cac2daad10e',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    symbol=data['data'][0]['symbol']
    print(symbol)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)




def get_id(symbol):
  cripto_symbol = symbol
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/map'
  parameters = {
    'symbol': cripto_symbol
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9484b998-5485-4933-b161-2cac2daad10e',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    id = data['data'][0]['id']
    return id
    #id=data[0]
    #print(id)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)




def get_quote():
  name=input('Enter the name of the cryptocurrency (ex: Bitcoin ou Ethereum): ')
  mes_passado=input('Enter date (ex: 14/06/1019): ')
  mes_passado_hora=mes_passado+' 8:00'
  data_e_hora = datetime.strptime(mes_passado_hora, '%d/%m/%Y %H:%M')

  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'
  parameters = {
    'name':name,
    'count':'1',
    'time_start':data_e_hora
    }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9484b998-5485-4933-b161-2cac2daad10e',
  }
  session = Session()
  session.headers.update(headers)
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    symbol=data
    print(symbol)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)



def get_report():
  symbol=input('Enter the symbol of the cryptocurrency (ex: btc): ')
  cripto_symbol = symbol.upper()
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/info'
  parameters = {
    'symbol': cripto_symbol,
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9484b998-5485-4933-b161-2cac2daad10e',
  }

  session = Session()
  session.headers.update(headers)
  
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data['data'][cripto_symbol])
    id=data['data'][cripto_symbol]['id']
    name=data['data'][cripto_symbol]['name']
    symbol=data['data'][cripto_symbol]['symbol']
    category=data['data'][cripto_symbol]['category']
    slug=data['data'][cripto_symbol]['slug']
    logo=data['data'][cripto_symbol]['logo']
    description=data['data'][cripto_symbol]['description']
    date_added=data['data'][cripto_symbol]['date_added']
    notice=data['data'][cripto_symbol]['notice']
    tags=data['data'][cripto_symbol]['tags']
    #Exibicao do relatorio
    print("\n" * os.get_terminal_size().lines)
    print('\n Relatorio de Criptomoeda \n')
    print('\n Codigo Id: %s \n' % id)
    print('\n Nome: %s \n' % name)
    print('\n Simbolo: %s \n' % symbol)
    print('\n Categoria: %s \n' % category)
    print('\n Slug: %s \n' % slug)
    print('\n Logotipo: %s \n' % logo)
    print('\n Descricao: %s \n' % description)
    print('\n Data de adicao ao sistema: %s \n' % date_added)
    print('\n Ultimas Noticias: %s \n' % notice)
    print('\n Tags: %s \n' % tags)
    print('\n Gerado Automaticamente por B.B.M. Crypto Analyser \n')
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def exhibition(symbol):
    cryptocurrency = symbol
   
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

        print(price)
        print(volume_24h)
        print(percent_change_1h)
        print(percent_change_24h)
        print(percent_change_7d)
        print(market_cap)

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

        print(website)
        print(technical_doc)
        print(id)
        print(name)
        print(symbol)
        print(category)
        print(slug)
        print(logo)
        print(description)
        print(date_added)
        print(notice)
        print(tags)
        print(explorer)
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


#get_symbol()
#get_id("btc")
#get_quote()
#get_report()
exhibition('XRP')
