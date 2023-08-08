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
   data = "男 test 2 星座"
   return data
# "\n爱情指数："+str(res["newslist"][1]["content"])+"\t工作指数："+str(res["newslist"][2]["content"])+"\n财运指数："+str(res["newslist"][3]["content"])+"\t健康指数："+str(res["newslist"][4]["content"])+"\n今日概述："+str(res["newslist"][8]["content"])

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

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
get_count()
#print(today.weekday())
wm = WeChatMessage(client)
# wea,temperature,low,high,dates,wind = get_weather()
# wea2,temperature2,low2,high2,dates2,wind2 = get_weather2()
# week_math = datetime.strptime(today,"%Y-%m-%d").weekday()
now_date = datetime.now().strftime('%Y-%m-%d')
data = {"city":{"value":city},
        "today":{"value":now_date + " 星期" + week(today.weekday())}, #今天日期

        "lucky":{"value":lucky(),"color":get_random_color()}, # 女方星座
        "birthday_left":{"value":get_birthday(),"color":get_random_color()}, # 女方生日
         "birthday_left2":{"value":get_birthday2(),"color":get_random_color()}, # 男方生日
        "love_days":{"value":get_count(),"color":get_random_color()}, # 恋爱日
         "words":{"value":get_words(), "color":get_random_color()} #彩虹屁
                
#         "weather":{"value":wea,"color":get_random_color()}, # 女方天气
#         "wind":{"value":wind,"color":get_random_color()}, # 女方天气风级
#         "temperature":{"value":temperature,"color":get_random_color()}, # 女方天气气温
#         "low":{"value":low,"color":get_random_color()}, # 女方天气低温
#         "high":{"value":high,"color":get_random_color()}, # 女方天气高温
     #    "words":{"value":"日出东方落于西，朝思暮想念于你", "color":get_random_color()} #彩虹屁
        
}

data2 = {"city":{"value":city2},
        "today":{"value":now_date + " 星期" + week(today.weekday())}, #今天日期
         "words":{"value":"word_92649898", "color":get_random_color()}, #彩虹屁
#         "weather2":{"value":wea2,"color":get_random_color()}, # 男方天气
#         "wind2":{"value":wind2,"color":get_random_color()}, # 男方天气风级
#         "temperature2":{"value":temperature2,"color":get_random_color()}, # 男方天气气温
#         "low2":{"value":low2,"color":get_random_color()}, # 男方天气低温
#         "high2":{"value":high2,"color":get_random_color()}, # 男方天气高温
        "birthday_left2":{"value":get_birthday2(),"color":get_random_color()}, # 男方生日
         "birthday_left":{"value":get_birthday(),"color":get_random_color()}, # 女方生日
       # "lucky2":{"value":"92649898","color":get_random_color()},  # 男方星座
      #   "words_star":{"value":"words_star_92649898","color":get_random_color()},
        "love_days":{"value":get_count(),"color":get_random_color()}, # 恋爱日

      #   "words":{"value":"日出东方落于西，朝思暮想念于你", "color":get_random_color()} #彩虹屁
}


#res = wm.send_template(user_id, template_id, data)  #发送
res2 = wm.send_template(user_id2, template_id2, data2)
res2 = wm.send_template(user_id2, template_id, data)
#print(res)
print(data2)
print(res2)





# 

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

#词霸每日一句
# def get_ciba():
#     if (Whether_Eng!="否"):
#         url = "http://open.iciba.com/dsapi/"
#         headers = {
#             'Content-Type': 'application/json',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#         }
#         r = get(url, headers=headers)
#         note_en = r.json()["content"]
#         note_ch = r.json()["note"]
#         return note_ch, note_en
#     else:
#         return "",""


# #彩虹屁
# def caihongpi():
#     if (caihongpi_API!="否"):
#         conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
#         params = urllib.parse.urlencode({'key':caihongpi_API})
#         headers = {'Content-type':'application/x-www-form-urlencoded'}
#         conn.request('POST','/caihongpi/index',params,headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = json.loads(data)
#         data = data["newslist"][0]["content"]
#         if("XXX" in data):
#             data.replace("XXX","蒋蒋")
#         return data
#     else:
#         return ""

# #健康小提示API
# def health():
#     if (health_API!="否"):
#         conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
#         params = urllib.parse.urlencode({'key':health_API})
#         headers = {'Content-type':'application/x-www-form-urlencoded'}
#         conn.request('POST','/healthtip/index',params,headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = json.loads(data)
#         data = data["newslist"][0]["content"]
#         return data
#     else:
#         return ""

#励志名言
# def lizhi():
#     if (lizhi_API!="否"):
#         conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
#         params = urllib.parse.urlencode({'key':lizhi_API})
#         headers = {'Content-type':'application/x-www-form-urlencoded'}
#         conn.request('POST','/lzmy/index',params,headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = json.loads(data)
#         return data["newslist"][0]["saying"]
#     else:
#         return ""
        

#下雨概率和建议
# def tip():
#     if (tianqi_API!="否"):
#         conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
#         params = urllib.parse.urlencode({'key':tianqi_API,'city':city})
#         headers = {'Content-type':'application/x-www-form-urlencoded'}
#         conn.request('POST','/tianqi/index',params,headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = json.loads(data)
#         pop = data["newslist"][0]["pop"]
#         tips = data["newslist"][0]["tips"]
#         return pop,tips
#     else:
#         return "",""

# #推送信息
# def send_message(to_user, access_token, city_name, weather, max_temperature, min_temperature, pipi, lizhi, pop, tips, note_en, note_ch, health_tip, lucky_):
#     url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
#     week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
#     year = localtime().tm_year
#     month = localtime().tm_mon
#     day = localtime().tm_mday
#     today = datetime.date(datetime(year=year, month=month, day=day))
#     week = week_list[today.isoweekday() % 7]
#     # 获取在一起的日子的日期格式




# host = 'https://freecityid.market.alicloudapi.com'
# path = '/whapi/json/alicityweather/briefcondition'
# method = 'POST'
# appcode = 'bd755a41eb7645a79c693f807d46d00f'
# querys = ''
# bodys = {}
# url = host + path

# bodys['cityId'] = city
# bodys['token'] = '''46e13b7aab9bb77ee3358c3b672a2ae4'''
# post_data = urllib.urlencode(bodys)
# request = urllib2.Request(url, post_data)
# request.add_header('Authorization', 'APPCODE ' + appcode)
# # 根据API的要求，定义相对应的Content-Type
# request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# response = urllib2.urlopen(request, context=ctx)
# content = response.read()
# if (content):
#     print(content)
    
# def get_weather(): # 女方天气
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   dates = weather['date']
#   return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high']),dates,weather['wind']

# def get_weather2(): #男方天气
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city2
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   dates = weather['date']
#   return weather['weather'], math.floor(weather['temp']),math.floor(weather['low']),math.floor(weather['high']),dates,weather['wind']
 
