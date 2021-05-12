import requests
from bs4 import BeautifulSoup
import json
def getreply(name):
    num=0
    replies=[]
    while True:
        print(num)
        link="https://www.82cat.com/tieba/reply/"+name+"/"+str(num)
        num+=1
        # try:
        r=requests.get(link,timeout=30)
        # except:
        #     break
        soup=BeautifulSoup(r.text,'lxml')
        liTags = soup.find_all('li', attrs={"class": 'mb-1'})
        if liTags == []:
            break
        for li in liTags:
            reply={}
            reply['ba']=li.find_all('a')[0].text.strip()
            reply['replyto'] = li.find_all('a')[1].text.strip()
            reply['time'] = li.find('span').text.strip()
            tig='在'+reply['ba']+'吧'
            tig2=reply['replyto']+'：'
            reply['content'] = li.text.strip().replace(tig,'')
            reply['content'] = reply['content'].replace(tig2, '')
            reply['content'] = reply['content'].replace(reply['time'], '')
            replies.append(reply)
    with open("data/"+name+".json","w",encoding="utf-8") as f:
        js=json.dumps(replies)
        f.write(js)
    return replies
if __name__ == '__main__':
    getreply("WenDavid_MPhI")


