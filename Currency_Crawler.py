import requests
from bs4 import BeautifulSoup
import json
import html.parser
import xmlrpc.client
import json



url = "https://www.eghtesadonline.com/feeds/"
h = html.parser.HTMLParser()
resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')

news_itemsa = []
a = 1
for item in items:
    
    news_item = {}
    d = BeautifulSoup(h.unescape(item.description.string))
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['img'] = d.img['src']
    news_itemsa.append(news_item)
    href = item.link.text
    test = item.title.text
#post one by one in wordpress
    
    print(test)
    a = {
    "title": "<a href="+item.link.text+" title="+test+">%s</a>" %test,
    "Author": "ali",
    "Categories":"اقتصادی",
    "Tags": item.link.text,
    "description": item.description.text 
}

    config = {
    'wp_url':"http://barootin.com/xmlrpc.php",
    'wp_username':"nadmin",
    'wp_password':'1234?qwer'
}

#Prepare post request options
    post_id = ""
    status_published = 1
#Making client request to wordpress site server
    server = xmlrpc.client.ServerProxy(config['wp_url'])
    

    post_id = server.metaWeblog.newPost(
        post_id, config['wp_username'],
        config['wp_password'],
        a,
        status_published)
    
    
    
with open('post.json', 'w') as fp:
    json.dump(news_itemsa, fp, indent=2)
    	

