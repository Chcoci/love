from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
from requests import get, post
import sys
import os
import http.client, urllib
import json
# from zhdate import ZhDate

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]
api_key_lucky = os.environ["API_KEY_LUCKY"]
astro = os.environ["ASTRO"]
#词霸每日一句
def get_ciba():
    if (Whether_Eng!="否"):
        url = "http://open.iciba.com/dsapi/"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        r = get(url, headers=headers)
        note_en = r.json()["content"]
        note_ch = r.json()["note"]
        return note_ch, note_en
    else:
        return "",""


#彩虹屁
def caihongpi():
    if (caihongpi_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':caihongpi_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/caihongpi/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        data = data["newslist"][0]["content"]
        if("XXX" in data):
            data.replace("XXX","蒋蒋")
        return data
    else:
        return ""

#健康小提示API
def health():
    if (health_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':health_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/healthtip/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        data = data["newslist"][0]["content"]
        return data
    else:
        return ""

#星座运势
# def lucky():
#     if (API_KEY_LUCKY!="否"):
#         conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
#         params = urllib.parse.urlencode({'key':API_KEY_LUCKY,'astro':astro})
#         headers = {'Content-type':'application/x-www-form-urlencoded'}
#         conn.request('POST','/star/index',params,headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = json.loads(data)
#         data = "\n爱情指数："+str(data["newslist"][1]["content"])+"   工作指数："+str(data["newslist"][2]["content"])+"\n今日概述："+str(data["newslist"][8]["content"])
#         return data
#     else:
#         return ""


def lucky():
  url = "http://api.tianapi.com/star/index?key=" + API_KEY_LUCKY +"&astro="+astro
  res = requests.get(url).json()
  data = "\n爱情指数："+str(res["newslist"][1]["content"])+"   工作指数："+str(res["newslist"][2]["content"])+"\n今日概述："+str(res["newslist"][8]["content"])
  return data


#励志名言
def lizhi():
    if (lizhi_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':lizhi_API})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/lzmy/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        return data["newslist"][0]["saying"]
    else:
        return ""
        

#下雨概率和建议
def tip():
    if (tianqi_API!="否"):
        conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
        params = urllib.parse.urlencode({'key':tianqi_API,'city':city})
        headers = {'Content-type':'application/x-www-form-urlencoded'}
        conn.request('POST','/tianqi/index',params,headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        pop = data["newslist"][0]["pop"]
        tips = data["newslist"][0]["tips"]
        return pop,tips
    else:
        return "",""

#推送信息
def send_message(to_user, access_token, city_name, weather, max_temperature, min_temperature, pipi, lizhi, pop, tips, note_en, note_ch, health_tip, lucky_):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    week = week_list[today.isoweekday() % 7]
    # 获取在一起的日子的日期格式

def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  dates = weather['date']
  return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high']),dates,weather['wind']
 
def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days + 1

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature,low,high,dates,wind= get_weather()
data = {"city":{"value":city},
        "today":{"value":dates}, #今天日期
        "weather":{"value":wea,"color":get_random_color()}, #天气
        "wind":{"value":wind,"color":get_random_color()}, #天气
        "temperature":{"value":temperature,"color":get_random_color()},
        "low":{"value":low,"color":get_random_color()},
        "high":{"value":high,"color":get_random_color()},
        "love_days":{"value":get_count(),"color":get_random_color()},
        "birthday_left":{"value":get_birthday(),"color":get_random_color()},
        "words":{"value":get_words(), "color":get_random_color()},
        "lucky":{"value":lucky(),"color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
