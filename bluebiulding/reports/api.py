from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from requests import Request, Session

def cryptoAPI(name, symbol):
    your_name = name
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
        'your_name' : your_name,
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
    return context