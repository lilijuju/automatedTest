import requests


# 打印响应主体内容，字符串格式

# 发送post请求
def post():
    res = requests.post(url='http://123.56.99.53:5000/event/weather/getWeather/',
                        headers={"Content-Type": "application/json"},
                        json={"theCityCode": "1001"})
    print(res.text)


# 发送get请求
def get():
    res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince')
    print(res.text)


if __name__ == '__main__':
    post()
    get()
