import numpy as np
import getcomment
import crackcrc32
import visit

videocode=input("请输入视频地址:")
list_ini=getcomment.getlist(videocode)
list_ini.soup()
list_ini.finder()
list_ini.getmark()
bullet=(input('请输入要查找的关键词:'))

all_bullet=list_ini.filterconcrete(bullet)
print(all_bullet)

all_crc32s=list_ini.getcrc32()
print(all_crc32s)

crackcrc32.create_table()

all_uid=[]
for ch in all_crc32s:
    temp=crackcrc32.main(ch)
    all_uid.append(temp)
print(all_uid)

all_space=[]
for ch in all_uid:
    temp=['http://space.bilibili.com/',ch]
    buffer=''.join(temp)
    all_space.append(buffer)
print(all_space)

user_nickname=visit.user_info(all_space)
nicknames=user_nickname.getnickname()