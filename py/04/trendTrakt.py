from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def getResponse(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if check_response(resp):
                return resp.content
            else:
                return None;
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def check_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1
            )

def log_error(e):
    print(e)

raw_html = getResponse('https://trakt.tv/shows/trending')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('h3')):
    '''for x, lst in enumerate(html.select('h4')):
        print(x, lst.text)'''
    print(i, li.text)