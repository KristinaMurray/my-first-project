from bs4 import BeautifulSoup
import requests
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': 'TS_think_language=zh-CN; TS_LOGGED_USER=C7hvlQbKDOcYOK8C43wfzZzA9; TS_oauth_token=7079b3910818cd98a1c5c7773554396b; TS_oauth_token_secret=6899cd3b13b9abc2310bcb4a7d9c634c'
}

urllist = []
for i in range(1679):
    url = 'https://sdust.pocketuni.net/index.php?app=event&mod=School&act=rank&k=3&p={page}'.format(page=i)
    urllist.append(url)


for url in urllist:
    r=requests.get(url,headers = headers)
    urllist.append(r)
    soup=BeautifulSoup(r.content,'html.parser')
    print(soup.name)
    t = soup.find_all(re.compile('^td'))

    for title in t:
        print(title.string)
        with open("2.txt", 'a', encoding='utf-8') as a:
            for j in range(18461):
                for k in range(4):
                    a.write(str(title.string)+',')
                a.write('\n')

