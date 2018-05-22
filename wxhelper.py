from Withdraw_message import *
from Auto_message import my_scheduler
import datetime as dt
import sys

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    temp = int(input('请输入您要开启的功能:') )
    if temp ==0:
        print('防止撤回消息的功能已经开启...')
        itchat.run()
    else:
        print('特别的爱给特别的人~')
        while 1:

            time_str = input('发送消息的时间[ex:2018-05-21 21:00:00]: ')
            now = dt.datetime.now()  # 获取当前时间
            nextTickTime = now.strftime(time_str)  # 把下一个问候时间设定为明天的零点
            # tick(userName=userName, meetDate=meetDate)
            my_scheduler(nextTickTime)  # 启用定时操作

            itchat.run()

