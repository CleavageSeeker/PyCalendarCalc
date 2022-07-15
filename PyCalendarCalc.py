import zhdate
from zhdate import ZhDate
from datetime import date

def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]

m = input('请选择1.公历→农历；2.农历→公历;3.今日：')

if (m == '1'):
    cal = input('请输入日期（XXXX-XX-XX）:')
    print("公历日期 " + cal + " 对应的农历日期为：")
elif (m == '2'):
    cal = input('请输入日期（XXXX-XX-XX）:')
    print("农历日期 " + cal + " 对应的公历日期为：")
elif (m == '3'):
    today = date.today()
    print("今天是： " + str(today.strftime("%Y年%m月%d日")) + ' ' + get_week_day(today) + ' | ' + str(ZhDate.today()))

else:
    print("输入规则写在那里，你瞎啊？")

