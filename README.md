# 每日早安推送给我的女朋友
## .github/workflows ：在此添加全局变量，格式参考其中就好
## main.py ： 运行的主函数

## 需要用到的全局变量（在Setting->Secrets->Action->New repository secret）中添加变量名和Value值

### API_KEY_LUCKY 星座API的Key，申请在 https://www.tianapi.com

### APP_ID  微信测试公众号的的APP_id

### APP_SECRET  测试号的 SECRET密钥

### ASTRO 女方星座，汉字即可

### STRO2 男方星座

### BIRTHDAY 女方生日 格式 01-01

### BIRTHDAY2 男方生日

### CITY 女方城市 区/市 均可

### CITY2 男方城市

### START_DATE 恋爱日 2022-02-02

### TEMPLATE_ID 女方模板ID

### TEMPLATE_ID2 男方模板ID

### USER_ID 女方用户ID

### USER_ID2 男方用户ID

微信模板内容示例：
宝贝~ 今天是 {{today.DATA}} 
{{city.DATA}}今日天气: {{weather.DATA,color.DATA}} {{wind.DATA,color.DATA}} 
当前气温: {{temperature.DATA,color.DATA}} ℃ 
今日温度: {{low.DATA}}~{{high.DATA,color.DATA}} ℃ 
在一起已经 {{love_days.DATA,color.DATA}} 天啦
距离宝贝生日还有 {{birthday_left.DATA,color.DATA}} 天 
距离我的生日还有 {{birthday_left2.DATA,color.DATA}} 天 
{{words.DATA,color.DATA}} {{lucky.DATA,color.DATA}}
