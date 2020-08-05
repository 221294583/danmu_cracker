import main
import os
import aboutme


while True:
    os.system('cls')
    print('1.开始使用','\n','2.作者信息','\n','y4exit')
    choice=str(input('输入数字1/2'))
    if choice=='1':
        main.process()
    elif choice=='2':
        aboutme.main()
    elif choice=='y' or choice=='Y':
        break;
    input('按任意键继续！')