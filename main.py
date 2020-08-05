import numpy as np
import getcomment
#import crackcrc32
import visit
import crack

def process():
    videocode=input("请输入视频地址:")
    list_ini=getcomment.getlist(videocode)
    list_ini.soup()
    list_ini.finder()
    list_ini.getmark()
    bullet=(input('请输入要查找的关键词:'))
    
    all_bullet=list_ini.filterconcrete(bullet)
    
    all_crc32s=list_ini.getcrc32()
    
    #crackcrc32.create_table()
    crack.main()
    
    all_uid=[]
    for ch in all_crc32s:
        temp=crack.crackl4(ch)[0]
        #print(type(temp))
        all_uid.append(temp)
    
    all_space=[]
    for ch in all_uid:
        temp=['http://space.bilibili.com/',ch]
        buffer=''.join(temp)
        all_space.append(buffer)
    
    user_nickname=visit.user_info(all_space)
    nicknames=user_nickname.getnickname()
    print('弹幕信息以及发送者信息:','\n')
    for i in range(len(all_bullet)):
        temp=['http://space.bilibili.com/',all_uid[i]]
        print('弹幕内容:',' ',all_bullet[i],'   ','用户昵称:',' ',nicknames[i],'   ','空间网址:',' ',(''.join(temp)))

    return all_bullet, all_crc32s, all_space, all_uid, bullet, ch, i, list_ini, nicknames, user_nickname, videocode
