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

#get_symbol()

def get_quote():
  name=input('Digite o nome da criptomoeda (ex: Bitcoin ou Ethereum): ')
  mes_passado=input('Digite a data (ex: 14/06/1019): ')
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

#get_quote()

def get_report():
  cripto_slug=input('Digite o nome da criptomoeda (ex: bitcoin ou ethereum): ')
  url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/info'
  parameters = {
    'slug': cripto_slug,
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
    print(data['data']['1'])
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

get_report()