import urllib.request

# file:///G:/python%20materials/%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2/09day/http%E5%8D%8F%E8%AE%AE.html

# coding = 'utf-8'

#get
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# #post
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# #超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/post",timeout=1,data=data)
#     print(response.read().decode("utf-8"))
# except:
#     print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders())
# print(response.getheader('Connection'))

# post 请求中修改user-agent
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}
req = urllib.request.Request("http://httpbin.org/post",data=data,headers = headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print(response.info())




