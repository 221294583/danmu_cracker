import urllib.request as req
from bs4 import BeautifulSoup
import gzip
from io import BytesIO
import lxml
import requests
import zlib
import re

class getlist:
    def __init__(self,videocode):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36'}
        website=req.Request(url=videocode,headers=headers)
        dataset=req.urlopen(website).read()
        print(dataset)
        buffer=BytesIO(dataset)
        temp=gzip.GzipFile(fileobj=buffer)
        self.cidinfo=temp.read().decode('utf-8')
    def soup(self):
        soup=BeautifulSoup(self.cidinfo,features="html.parser")
        writer=str(soup)
        with open('datamoeg.txt','w',encoding='utf-8') as temp:
            temp.write(writer)
    def finder(self):
        with open('datamoeg.txt','r',encoding='utf-8') as temp:
            lines=temp.read()
        first_cid=lines.find('"cid"')
        first_cid+=6
        cid_numline=[]
        while True:
            temp=lines[first_cid]
            if temp==',':
                break
            cid_numline.append(temp)
            first_cid+=1
        self.cid=''.join(cid_numline)
        print(self.cid,'\n',type(self.cid))
    def getmark(self):
        loc_list=['http://comment.bilibili.com/',self.cid,'.xml']
        loc=''.join(loc_list)
        print(loc)
        website=requests.get(url=loc)
        dataset=website.content
        soup=BeautifulSoup(dataset,features="xml")
        writer=str(soup)
        with open('datacom.txt','w',encoding='utf-8') as temp:
            temp.write(writer)
        ds=soup.find_all('d')
        contents=[]
        infos=[]
        for buffer in ds:
            contents.append(buffer.string)
            infos.append(buffer.attrs)
        self.cominfo=infos
        self.content=contents
        print(contents,'\n',type(contents),'\n',infos,'\n',type(infos[0]))
    def filterconcrete(self,bullet):
        com_carrier=[]
        index_carrier=[]
        for i in range(len(self.content)):
            print(self.content[i])
            if self.content[i].find(bullet)!=-1:
                com_carrier.append(self.content[i])
                index_carrier.append(i)
        self.index=index_carrier
        return com_carrier
    def getcrc32(self):
        index_carrier=self.index
        crc32s=[]
        for i in range(len(index_carrier)):
            seq=index_carrier[i]
            prep=self.cominfo[seq]['p']
            count=0
            crc32seq=[]
            for ch in prep:
                if count==6 and ch!=',':
                    crc32seq.append(ch)
                if ch==',':
                    count+=1
            temp=''.join(crc32seq)
            crc32s.append(temp)
        return crc32s
