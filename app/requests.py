from app import app
import urllib.request,json
from .models import Quote


base_url = 'http://quotes.stormconsultancy.co.uk/random.json'


def get_quotes():

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_result = None

        

    

    return quote_result

def process_results(quote_list):

    quote_result = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')


    return quote_result