from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.facebook.com/hashtag/bihu').text

soup = BeautifulSoup(html_text, 'lxml')
print(soup)
posts = soup.find_all(class_='rq0escxv l9j0dhe7 du4w35lb qmfd67dx hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5')
post = soup.find(class_='rq0escxv l9j0dhe7 du4w35lb qmfd67dx hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5')

print(post)
