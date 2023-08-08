from datetime import date, datetime
import math 
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random


app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]
template_id = os.environ["TEMPLATE_ID"]
template_id2 = os.environ["TEMPLATE_ID2"]
today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
city2 = os.environ['CITY2']
birthday = os.environ['BIRTHDAY']
birthday2 = os.environ['BIRTHDAY2']
astro = os.environ["ASTRO"]
astro2 = os.environ["ASTRO2"]
user_id = os.environ["USER_ID"]
user_id2 = os.environ["USER_ID2"]

api_key_lucky = os.environ["API_KEY_LUCKY"]


def week(a):
    if a==0:data = "一"
    if a==1:data = "二"
    if a==2:data = "三"
    if a==3:data = "四"
    if a==4:data = "五"
    if a==5:data = "六"
    if a==6:data = "日"
    return data

def lucky(): # 女方星座
   url = "http://api.tianapi.com/star/index?key=" + api_key_lucky +"&astro="+astro
   res = requests.get(url).json()
   data = "\n爱情指数："+str(res["newslist"][1]["content"])+"   工作指数："+str(res["newslist"][2]["content"])+"\n财运指数："+str(res["newslist"][3]["content"])+"   健康指数："+str(res["newslist"][4]["content"])+"\n今日概述："+str(res["newslist"][8]["content"])
   return data

def lucky2(): # 男方星座
   url = "http://api.tianapi.com/star/index?key=" + api_key_lucky +"&astro="+astro2
   res = requests.get(url).json()
   data = "爱情指数："+str(res["newslist"][1]["content"]) + "  工作指数："+str(res["newslist"][2]["content"])
   return data
# "\n爱情指数："+str(res["newslist"][1]["content"])+"\t工作指数："+str(res["newslist"][2]["content"])+

def lucky2_2(): # 男方星座
   url = "http://api.tianapi.com/star/index?key=" + api_key_lucky +"&astro="+astro2
   res = requests.get(url).json()
   data = "\n财运指数："+str(res["newslist"][3]["content"])+"\t健康指数："+str(res["newslist"][4]["content"])
   return data
# def lucky2_3(): # 男方星座 今日概况
#    url = "http://api.tianapi.com/star/index?key=" + api_key_lucky +"&astro="+astro2
#    res = requests.get(url).json()
#    data = str(res["newslist"][8]["content"])
#    return data    
    
def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days + 1

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days + 1

def get_birthday2():
  next = datetime.strptime(str(date.today().year) + "-" + birthday2, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days + 1

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']
    
client = WeChatClient(app_id, app_secret)
get_count()
#print(today.weekday())
wm = WeChatMessage(client)
# wea,temperature,low,high,dates,wind = get_weather()
# wea2,temperature2,low2,high2,dates2,wind2 = get_weather2()
# week_math = datetime.strptime(today,"%Y-%m-%d").weekday()
now_date = datetime.now().strftime('%Y-%m-%d')
data = {
        "today":{"value":now_date + " 星期" + week(today.weekday())}, #今天日期
        "lucky":{"value":lucky()}, # 女方星座
        "birthday_left":{"value":get_birthday()}, # 女方生日
         "birthday_left2":{"value":get_birthday2()}, # 男方生日
        "love_days":{"value":get_count()}, # 恋爱日
         "words":{"value":get_words()} #彩虹屁       
}

data2 = {
        "today":{"value":now_date + " 星期" + week(today.weekday())}, #今天日期
         "words":{"value":get_words()}, #彩虹屁
        "birthday_left2":{"value":get_birthday2()}, # 男方生日
         "birthday_left":{"value":get_birthday()}, # 女方生日
        "lucky2":{"value":lucky2()},  # 男方星座指数1
        "lucky2_2":{"value":lucky2_2()},  # 男方星座指数2
        # "lucky2_3":{"value":lucky2_3()},  # 男方星座今日概况
        "love_days":{"value":get_count()}, # 恋爱日

      #   "words":{"value":"日出东方落于西，朝思暮想念于你", "color":get_random_color()} #彩虹屁
}


#res = wm.send_template(user_id, template_id, data)  #发送
res2 = wm.send_template(user_id2, template_id2, data2)
res2 = wm.send_template(user_id2, template_id, data)
#print(res)
print(data2)
print(res2)





