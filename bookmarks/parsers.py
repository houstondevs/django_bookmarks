import requests
from bs4 import BeautifulSoup as bs
from testcase.celery import app
from .models import Book
from django.contrib.auth import get_user_model
from urllib.request import urlopen
from testcase.settings import BASE_DIR

User = get_user_model()

@app.task()
def parse(url, email):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }

    data = {}

    session = requests.Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:

        soup = bs(request.content, 'html.parser')
        title = soup.find('title').text
        try:
            favicon = soup.find('link', attrs={'rel': 'icon'})['href']
            if 'http' or 'https' in favicon:
                pass
            else:
                favicon = url + favicon
        except:
            favicon = "Нету favicon"

        try:
            description = soup.find('meta', attrs={'name': 'description'})['content']
        except:
            description = 'описание не указано'

        data = {
            'title': title,
            'description': description,
            'favicon': favicon
        }
        user = User.objects.get(email=email)
        Book.objects.create(user=user, url=url, title=data['title'], description=data['description'],
                            favicon=data['favicon'])

    else:
        print('ERROR')

    return data
