import requests
def title(url):
     a=requests.get(url)
     t=a.text
     t=t.split('</title>')
     t=t[0].split('<title>')
     return t[1].replace(' - YouTube','')
print(title(input('please insert url')))