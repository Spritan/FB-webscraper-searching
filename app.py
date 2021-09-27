from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.facebook.com/hashtag/bihu').text

