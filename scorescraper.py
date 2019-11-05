from bs4 import BeautifulSoup
import urllib.request
from playsound import playsound
import subprocess as s
import time

def get_score(selected_names):
    s.call(['notify-send','127 Scraper','Starting scrape.'])
    playsound('updated.ogg')
    page = urllib.request.urlopen('https://www2.cs.sfu.ca/CourseCentral/127/common/results/')

    content = page.read()
    soup = BeautifulSoup(content, features="html.parser")
    date = soup.p.contents[0][27:51]
    print(date)

    table = soup.find_all('table')[0]

    for row in table.find_all('tr'):
            cols = row.find_all('th')
            name = ""
            passed = 0;
            total = 0;
            for col in cols:
                if col.has_attr('style') and col['style'] == "text-align:left;":
                    name = col.get_text()
                    for task in row.find_all('td'):
                        if task.has_attr('class'):
                            if task['class'][0] == "Pass":
                                passed += 1
                                total += 1
                            elif task['class'][0] == "Fail":
                                total += 1
            if name in selected_names:
                return name + ": " + str(passed) + "/" + str(total)