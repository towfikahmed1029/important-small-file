import traceback
### Try catch Function For find line Number
try:
    00000/0000000
except:
    print(traceback.format_exc())
### First Line Catch
def firstline():
    lines = []
    with open(r"t1.txt", 'r') as fp:
        lines = fp.readlines()
    with open(r"t1.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number != 0:
                fp.write(line)
    return lines[0].replace("\n","")
import requests
import re
from bs4 import BeautifulSoup

headers = { 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# Email Get
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


