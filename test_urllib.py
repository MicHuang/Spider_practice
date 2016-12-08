import urllib.request
import http.cookiejar

url = 'https://www.giuem.com/'
#第一种方法
response1 = urllib.request.urlopen(url)

print('First method:')
print(response1.getcode())
print(len(response1.read()))
print()

#第二种方法
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)

print('Second method:')
print(response2.getcode())
print(len(response2.read()))
print()

#第三种方法
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)

print('Third method:')
print(response3.getcode())
print(cookie)
print(response3.read())
