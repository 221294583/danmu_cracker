import requests
from bs4 import BeautifulSoup
import lxml

class user_info:
    def __init__(self,all_space):
        self.space_request=all_space
    def getnickname(self):
        nicknames=[]
        for space_loc in self.space_request:
            website=requests.get(space_loc)
            dataset=website.content
            soup=BeautifulSoup(dataset,features='lxml')
            temp=soup.find(attrs={'name':'keywords'})
            buffer=temp.attrs['content']
            loc=buffer.find(',')
            info=buffer[:loc]
            print(info)
            nicknames.append(info)
        return nicknames