from bs4 import BeautifulSoup
import urllib.request
from playsound import playsound
import subprocess as s
import time
from  scorescraper import get_score

s.call(['notify-send','127 Scraper','Starting scrape.'])
playsound('start.ogg')
page = urllib.request.urlopen('https://www2.cs.sfu.ca/CourseCentral/127/common/results/')

content = page.read()
soup = BeautifulSoup(content, features="html.parser")
date = soup.p.contents[0][27:51]
print(date)

while(1):
    time.sleep(5)
    page = urllib.request.urlopen('https://www2.cs.sfu.ca/CourseCentral/127/common/results/')
    content = page.read()
    soup = BeautifulSoup(content, features="html.parser")
    newdate = soup.p.contents[0][27:51]
    if newdate != date:
        s.call(['notify-send', 'CMPT 127 Scoreboard Updated.', get_score(['bobby-tables'])])
        playsound('updated.ogg')
        date= newdate
