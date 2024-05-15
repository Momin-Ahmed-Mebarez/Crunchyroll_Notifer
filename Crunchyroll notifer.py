from datetime import datetime,date
from Animes import *
from plyer import notification
import time












#fetchRoll()
#fetchEpisodes


content = open("mark.txt","r").read()

episodes = fetchEpisodes()
with open("mark.txt","a") as f:
    for episode in episodes:
        if(episode.time < datetime.now().time() and episode.name not in content):
            f.write("\n"+episode.name+"\n")
            notification.notify(title = "A new episode dropped",message=episode.name ,timeout=6)
            time.sleep(6)

 

 




