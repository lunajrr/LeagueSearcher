import data as Consts
import requests 
from webscraper import *


class RiotAPi(object):
    champList = {}
    
    #Constructor
    def __init__(self, api_key, region=Consts.REGIONS["North America"]):
        self.api_key = api_key
        self.region = region
    
    #Requests data from apis
    def _request(self, api_url, params=None):
        if params is None:
            params = {}
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(Consts.URL['Base'].format(region=self.region, url=api_url))

        return response.json()
    
    #gets account info from the summoners User Name
    def __look_up_summoner_by_name(self, name):
        api_url = Consts.URL['SummonerByName'].format(Version=Consts.APIVersions['SummonerByName'], summonerName=name, APIKEY=self.api_key)
        return self._request(api_url)
    
    #Gets summoner account info by name
    def get_summoner_by_name(self, name):
        summonerData = self.__look_up_summoner_by_name(name)
        try:
            self.SummonerID = summonerData['id']
        except KeyError:
            return -1, -1
        except NameError:
            return -1, -1
        return summonerData['id'], summonerData['summonerLevel']  
       
    #Get the json file from the list of champs    
    def get_champs(self):
        response = requests.get(Consts.championURL['Base'].format(Name='champion.json'))
        data = response.json()
        self.champList = data['data']
    
    #Get the top 3 most play champs from the summoner using the summoner id(Needs to run ouput_summoner_byName to get id*Fix LAter)    
    def __get_topThreeChamps(self):
        
        response = requests.get(Consts.URL['Base'].format(region=self.region, url=Consts.URL['ChampsByMastery'].format(Version=Consts.APIVersions['ChampMastery'],SummonerID=self.SummonerID,APIKEY=self.api_key)))
        data = response.json()
        top3Champs = []
        masteryForChamps = []
        for x in range(3):
            top3Champs.append(Consts.champId[data[x]['championId']])
            masteryForChamps.append(data[x]['championPoints'])
        return top3Champs, masteryForChamps    
   
   #Runs all necessary methods to output summoner name/level/top3 champs/ and win rate 
    def output_summoner_info(self, summonerName):
        
        #using methods to get summoner info
        summonerId, summonerLevel =self.get_summoner_by_name(summonerName)
        if summonerId == -1:
            return -1, -1, -1, -1
        top3Champs, masteryForChamps = self.__get_topThreeChamps()
        
        #Winrate is used by web scraping op.gg (only works for NA RIght now)
        ws = webscraper(self.region.replace("1", ""), summonerName.replace(" ", "+"))
        soloWinRatio = ws.get_solo_ranked_winrate()
        
        #Outputing The Infomation
        return summonerLevel, soloWinRatio,top3Champs, masteryForChamps
        