from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.facebook.com/hashtag/bihu').text

soup = BeautifulSoup(html_text, 'lxml')

posts = soup.find_all(class_='rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs')
post = soup.find(class_='rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs')

print(post)
