from bs4 import BeautifulSoup
import requests


class webscraper(object):
    
    #Constructor, sets the URL and requests/parses it
    def __init__(self, region, summonerName):
        global soup
        URL = "https://" + region + ".op.gg/summoner/userName="+ summonerName
        info = requests.get(URL)
        soup = BeautifulSoup(info.content, 'html.parser')
        
    
    #Searches HTML Code for the overall soloranked win ratio
    def get_solo_ranked_winrate(self):  
        global soup  
        results = soup.find(class_='winratio')
        #To see if we couldn't find the win rate
        if results == None:
            winRatio = "Error: Couldn't find win ratio on op.gg"
        else: 
            winRatio = results.text.replace("Win Ratio ", "")
        return winRatio
        
    
    def get_win_ratio_top_champs(self):
        return True
        