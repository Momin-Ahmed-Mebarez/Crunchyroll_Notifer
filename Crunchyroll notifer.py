from datetime import datetime,date
from Animes import *
from plyer import notification
import time

#The main function that handles notifications
def notify():
    #Read the mark folder (used to mark notified animies so the program doesn't notify twice for the same anime)
    content = open("mark.txt","r").read()
    
    #Calling fetchEpisodes from Animes 
    episodes = fetchEpisodes()
    with open("mark.txt","a") as f:
        for episode in episodes:
            #If the episode is not notified before and is avalible you will get a notification and will be added to mark file
            if(episode.time < datetime.now().time() and episode.name not in content):
                f.write("\n"+episode.name+"\n")
                notification.notify(title = "A new episode dropped",message=episode.name ,timeout=6, toast=True)
                time.sleep(6)
                
#The main loop to check every while
def task():
    sFetch = datetime.now()
    sCheck = datetime.now()
    eFetch = sFetch
    eCheck = sCheck
    delta = 0
    while(True):
        delta = eFetch - sFetch
        delta = delta.total_seconds()
        #Every two hours the program will fetch episodes from CrunchyRoll edit the(>= 2) by any number to reduce or increase the delay
        if(delta == 0.0 or (delta / (60*60)) >=  2): 
            sFetch = datetime.now()
            fetchRoll()
            eFetch = datetime.now()
        else:
            eFetch = datetime.now()
        #Every two minutes the program will check if any of the fetched animies is now avaliable
        delta = eCheck - sCheck
        delta = delta.total_seconds()
        if(delta == 0.0 or (delta / (60)) >=  2):
            sCheck = datetime.now()
            notify()
            time.sleep(1)
            eCheck = datetime.now()
        else:
            eCheck = datetime.now() 
 


if __name__ == "__main__":
    task()
