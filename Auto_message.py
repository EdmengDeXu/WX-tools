import itchat
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random



def my_scheduler(runTime):

    #users = itchat.search_friends(name=u'熊酱')  # 找到你女朋友的名称
    name = input(u'请输入对象的备注名:')
    users = itchat.search_friends(name = name)
    userName = users[0]['UserName']

    #meetDate = dt.date(2015, 9, 29)  # 这是你跟你女朋友相识的日期
    year = int(input('输入相识的年份:'))
    month = int(input('输入相识的月份:'))
    date = int(input('那天是几号？:'))
    meetDate = dt.date(year, month, date)
    greetList = []
    greetList.append(input('请输入你要对Ta说的话:'))
    scheduler = BackgroundScheduler()  # 生成对象
    scheduler.add_job(tick, 'date', run_date=runTime,args=[userName,meetDate,greetList])  # 在指定的时间，只执行一次
    scheduler.start()


def tick(userName,meetDate,greetList):

    nowDate = dt.date.today()  # 今天的日期
    passDates = (nowDate - meetDate).days  # 你跟你女朋友认识的天数
    itchat.send(u'今天是我们认识第%d天，%s' % (passDates, random.sample(greetList, 1)[0]), toUserName=userName)  # 发送问候语给女朋友
    # now = dt.datetime.now()  # 现在的时间
    # nextTickTime = now + dt.timedelta(days=1)
    # nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")
    # my_scheduler(nextTickTime)  # 设定一个新的定时任务，明天零点准时问候



