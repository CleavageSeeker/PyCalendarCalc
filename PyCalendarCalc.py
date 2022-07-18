from zhdate import ZhDate
import datetime
import string


def get_weekday(date):
    weekday_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    return weekday_dict[date.weekday()]

m = input('请选择1.公历→农历；2.农历→公历;3.今日：')
cal = input('\n请输入日期（YYYY-MM-DD/YYYYMMDD）:')

if (cal.find('-') > 0):
    cal = cal.replace('-', '')

strcal = [cal[0:4], cal[4:6], cal[6:8]]

if (m == '1'):
    cal = strcal[0] + '年' + strcal[1] + '月' + strcal[2] + '日'
    dateG = datetime.datetime(int(strcal[0]), int(strcal[1]), int(strcal[2]))
    print("\n公历 " + cal + " 对应的农历日期为：" + str(ZhDate.from_datetime(dateG)))
elif (m == '2'):
    cal = str(ZhDate(int(strcal[0]), int(strcal[1]), int(strcal[2])))
    dateN = ZhDate(int(strcal[0]), int(strcal[1]), int(strcal[2]))
    print("\n农历 " + cal + " 对应的公历日期为：" + str(ZhDate.to_datetime(dateN).date()))
elif (m == '3'):
    today = datetime.date.today()
    print("\n今天是：\t" + str(today.strftime("%Y年%m月%d日")) + ' ' + get_weekday(today) + '\n\t\t农历 ' + str(ZhDate.today().chinese()))
else:
    print("输入规则写在那里，你瞎啊？")

