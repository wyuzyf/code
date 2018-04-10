import requests
# user_agents={
#     'Host':'www.uustv.com',
#     'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
#     'Referer':'"http://www.uustv.com/"',
#     'Connection':'keep-alive'
# }
url = 'http://www.jiqie.com/i/38/1454.gif?032611375952451'
response = requests.get(url).content
print(response)
with open('will.gif', 'wb') as f:
    f.write(response)
# try:
#     im = Image.open('{}.gif'.format(name.decode('utf-8').encode('gbk')))
#     im.show()
# except:
#     print('自己打开看吧')

