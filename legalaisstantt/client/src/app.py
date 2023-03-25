from random import shuffle
from html.parser import HTMLParser
import time
import requests

http_session = requests.Session()
http_session.headers.update({'Authorization': 'Token 1a6783768326283428fc7689f3477087ec7ceee9'})




def search(query_dict):
    print('Performing search: %s' % query_dict)
    keyword = query_dict['keyword']
    page = query_dict['page']
    time.sleep(5)
    response = http_session.post('https://api.indiankanoon.org/search/?formInput=%s&pagenum=%s' % (keyword, page))
    resp_json = response.json()
    for doc in resp_json['docs']:
        add_doc(doc['tid'])
    for category in resp_json['categories']:
        if 'Related Queries' in category:
            for item in category[1]:
                add_search({'keyword': item['value'], 'page': 0})
    if page < 20:
        add_search({'keyword': keyword, 'page': page + 1})


def load_doc(doc_id):
    time.sleep(5)
    response = http_session.post('https://api.indiankanoon.org/doc/%s/' % doc_id)
    resp_json = response.json()
    index = resp_json['divtype']
    del resp_json['divtype']






    if __name__ == '__main__':
    main()
