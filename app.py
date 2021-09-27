from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://mobile.facebook.com/search/posts/?q=%23bihu&source=filter&isTrending=0&tsid=0.9934930337593051').text

soup = BeautifulSoup(html_text, 'lxml')
print(soup)

#posts = soup.find_all(class_='rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs')
#post = soup.find(class_='rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs')

# published_date = post.find('a', class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p').span.text
# print(published_date)
