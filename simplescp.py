from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from time import sleep
try:
    html = urlopen('https://coinranking.com/')
    bs = BeautifulSoup(html.read(), 'lxml')
    # print(bs.body.div.div.div.div)
    table_rows = bs.find_all('div',{'class':'valuta'})
    # print(table_rows[0:10:2])
    for i in range(0,10,2):
        print(f"{i}===========================")
        # print(table_rows[i])
        # print(table_rows[i].get_text())
        price_string = table_rows[i].get_text().replace('$','').replace(' ','').replace('\n','').replace(',','')
        price = float(price_string)
        print(price)
        print("************************")
except URLError as e:
    print('you should connect ot internt')
    sleep(1)

