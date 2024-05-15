from datetime import datetime,date
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





def fetchEpisodes():
    with open("daily.txt","r") as f:
        episodes = []
        for line in f:
            line = line.strip().split(" ")
            epTime = datetime.strptime(line[1], "%I:%M%p").time()
            episodes.append(Episode(line[0],epTime))
    return episodes







#Fetching from internet and saving
def fetchRoll():
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    
    #Storing the html from the page 
    driver.get("https://www.crunchyroll.com/simulcastcalendar?filter=premium")
    html = driver.page_source
    driver.quit()

    #Parsing the page as html
    page = BeautifulSoup(html, "html.parser")
    
    #Fetching the element we need (The episodes elements)
    page = page.find("ol",class_="days")
    page = page.find("li",class_="day active today")
    episodesList = page.find_all("article",class_="release js-release")

    #Creating object from every episode to store it locally
    for episode in episodesList:
        time = episode.find("time",class_="available-time")
        name = episode.find("cite")
        episodes.append(Episode(name.text.strip().replace(" ","_"),time.text.strip()))

    #Writing the episodes to a file
    with open("daily.txt","w") as f:
        for episode in episodes:
            f.write(episode.name + " " + episode.time + "\n")

    today = open("mark.txt","r").readline()
    if(today != str(date.today())):
        open("mark.txt","w").write(str(date.today()))


