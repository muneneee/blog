from app import app
import urllib.request,json
from .models import Quote


base_url = app.config['QUOTES_API_BASE_URL']


def get_quotes():

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_result = None

        if get_quotes_response['results']:
            quote_result_list = get_quotes_response['results']
            quote_result = process_results(quote_result_list)

    

    return quote_result