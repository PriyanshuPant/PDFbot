import json
import requests

url = "http://127.0.0.1:8000/response"
query = input('Query: ')

while query != 'q':

    params = {"query": f"{query}"}
    response = requests.get(url, params=params)

    try:

        [answer, page_no] = json.loads(response.text)

        print(f'Bot: {answer} ')
        if page_no != 'none':
            print(f'Page: {page_no}')

    except:
        print(json.loads(response.text))

    query = input('Query: ')
