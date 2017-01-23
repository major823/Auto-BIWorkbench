import requests

para = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=para)
print r.url