import time
from bs4 import BeautifulSoup
import selenium as se
from selenium import webdriver

episodes = []

class Episode:
    def __init__(self,name,time,episode="placeHolder",link="placeHolder"):
        self.name = name
        self.time = time

    def __str__(self):
        return f"Episode {self.name} at {self.time}"



options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.crunchyroll.com/simulcastcalendar?filter=premium")
html = driver.page_source
driver.quit()

page = BeautifulSoup(html, "html.parser")

page = page.find("ol",class_="days")
page = page.find("li",class_="day active today")

episodesList = page.find_all("article",class_="release js-release")

for episode in episodesList:
    time = episode.find("time",class_="available-time")
    name = episode.find("cite")
    episodes.append(Episode(name.text.strip(),time.text.strip()))


print(episodes[0])



