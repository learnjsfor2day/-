from bs4 import BeautifulSoup
import requests

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup= BeautifulSoup(demo,"html.parser")
print(soup.title)
tag=soup.a
print(tag)

print(soup.a.name,soup.a.parent.name)

print(tag.attrs)
"""标签属性"""
"""获得class属性"""
print(tag.attrs['class'])

print(type(tag.attrs))

print(type(tag))


