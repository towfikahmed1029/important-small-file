
    url = f"https://www.bing.com/images/search?q={key}&form=HDRSC2" # search URL for image results

    response = requests.get(url)
    for _ in range(6):
        soup = BeautifulSoup(response.content, "html.parser")
        response = requests.get(url, headers={"Range": "bytes=100-"})
        results = soup.find_all("div", class_="imgpt")


import re
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def get_email(url):
    try:
        domain = url.split('//')[-1].replace('www.', '').split('/')[0]
        url_gen = f'http://www.skymem.info/srch?q={domain}'
        response = requests.get(url_gen, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        email_list = re.findall(r"href=\"\/srch\?q=(.*?@.*)\">", str(soup))
        email = [line for line in email_list if domain in line][0]

        return email
    except:
        #print(traceback.format_exc())
        return None
