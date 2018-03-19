# Foxter @ 19/03/2018 - 8:39PM
# Забираем две страницы последних валлпаперов с wallhaven.
# Для работы также нужна bs4: pip install bs4


from bs4 import BeautifulSoup
from urllib.request import *

# вы можете также использовать ссылку на свои избранные валлпаперы, если предварительно расшарите их на сайте. По-умолчанию они приватны и скрыты.

url='https://alpha.wallhaven.cc/latest?page='


def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range (1,2):
        html = get_html(url+str(i))
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find_all(class_='preview')
        for a in list:
            secondary_html = get_html(a['href'])
            secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            image = secondary_soup.find(id='wallpaper')['src']
            urlretrieve('https:' + image, image[52:])
            print(image[52:], 'done')


main()
