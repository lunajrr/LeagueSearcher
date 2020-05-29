from RiotAPI import RiotAPi
from tkinter import * 
from tkinter.ttk import *

#only supports NA so far

#NEEds to be updated every 24 hours
api = RiotAPi("RGAPI-e1c0a10e-47e1-4ec4-a707-744c3679742f")
    
def search(userInput):
    global api, summonerName, summonerlvl, solowinRatio, topChamp1, topChamp2, topChamp3, mastery1, mastery2, mastery3, errorr
    summonerrlvl, solowinratio, top3Champs, masteryforChamps =api.output_summoner_info(userInput)
    
    if summonerrlvl == -1:
        errorr.set("Error with getting summoner ID")
    else:    
        summonerName.set(userInput)
        summonerlvl.set(summonerrlvl)
        solowinRatio.set(solowinratio)
        topChamp1.set(top3Champs[0])
        topChamp2.set(top3Champs[1])
        topChamp3.set(top3Champs[2])
        mastery1.set(str(masteryforChamps[0]) + " points")
        mastery2.set(str(masteryforChamps[1]) + " points")
        mastery3.set(str(masteryforChamps[2]) + " points")
        errorr.set("")
    
    
      
    
def run():
    global summonerName, summonerlvl, solowinRatio, topChamp1, topChamp2, topChamp3, mastery1, mastery2, mastery3, errorr
    
    # creating main tkinter window/toplevel 
    master = Tk() 
    master.title("League helper")
    #Variable Strings to update labels automatically
    summonerName, summonerlvl, solowinRatio = StringVar(), StringVar(), StringVar()
    topChamp1, topChamp2, topChamp3 = StringVar(), StringVar(), StringVar()
    mastery1, mastery2, mastery3 = StringVar(), StringVar(), StringVar()
    errorr = StringVar()
    #Setting the variable texts default values
    summonerName.set("")
    summonerlvl.set("")
    solowinRatio.set("")
    topChamp1.set("")
    topChamp2.set("")
    topChamp3.set("")
    mastery1.set("")
    mastery2.set("")
    mastery3.set("")
    errorr.set("")
    
    # label widget 
    searchSummonerLBL = Label(master, text = "Search Summoner") 
    ###Summoner Name
    summonerNameLBL = Label(master, text= "Summoner Name: ")
    enteredNameLbL = Label(master, textvariable=summonerName)
    ###SummonerLevel
    summonerLvlLbl = Label(master, text= "Summoner Level:")
    searchedSumlvlLBL= Label(master, textvariable=summonerlvl)
    ###Summoner Win Ratio
    winRatioLBL = Label(master, text= "Win Ratio:")
    summonerwinLBL = Label(master, textvariable=solowinRatio)
    ###topChamps
    topChampTXt = Label(master, text= "Top 3 Champions: ")
    topChamp1LBL = Label(master,textvariable=topChamp1)
    topChamp2LBL = Label(master,textvariable=topChamp2)
    topChamp3LBL = Label(master,textvariable=topChamp3)
    ###Mastery
    masterytxt = Label(master, text= "           Mastery: ")
    top1mastLBL = Label(master, textvariable=mastery1)
    top2mastLBL = Label(master, textvariable=mastery2)
    top3mastLBL = Label(master, textvariable=mastery3)
    ###ERror output
    errLBL = Label(master, textvariable = errorr)

    #Arranging labels in grid layout
    ##Search
    searchSummonerLBL.grid(row = 0, column = 0, sticky = W, pady = 20, padx = 10) 
    ##Summoner Name
    summonerNameLBL.grid(row = 1, column = 0, sticky = W, pady = 10, padx = 10) 
    enteredNameLbL.grid(row = 1, column = 1, sticky = W, pady = 10, padx = 0)
    ##SummonerLevel
    summonerLvlLbl.grid(row = 1, column= 2, sticky = W, pady = 10, padx = 0)
    searchedSumlvlLBL.grid(row=1, column =3, sticky = W, pady = 10, padx = 0)
    ##Win Ratio
    winRatioLBL.grid(row = 2, column=0, sticky = W, pady  = 10, padx=10)
    summonerwinLBL.grid(row=2, column=1, sticky = W, pady = 10, padx=0)
    ##Top 3 Champs
    topChampTXt.grid(row = 3, column = 0, sticky = W, pady = 10, padx=10)
    topChamp1LBL.grid(row = 3, column = 1, sticky = W, pady = 5, padx =0)
    topChamp2LBL.grid(row = 4, column = 1, sticky= W, pady = 5, padx =0)
    topChamp3LBL.grid(row = 5, column = 1, sticky = W, pady = 5, padx =0)
    ##Top 3 champs Mastery
    masterytxt.grid(row=3, column = 2, sticky= W, pady= 10, padx=0)
    top1mastLBL.grid(row=3, column = 3, sticky = W, pady=5, padx=0)
    top2mastLBL.grid(row=4, column = 3, sticky = W, pady=5, padx=0)
    top3mastLBL.grid(row=5, column = 3, sticky = W, pady=5, padx=0)
    ##Error
    errLBL.grid(row=6, sticky=W, pady=5, padx=0)
    
    
    # entry widgets, used to take entry from user
    searchSummonerEntry = Entry(master) 
  
    # this will arrange entry widgets 
    searchSummonerEntry.grid(row = 0, column = 1, pady = 10, padx = 20) 
    
    # Button widget
    searchSummonerBtn = Button(master, text = "Search",command=lambda:search(searchSummonerEntry.get()))
    
    #Arrange the button widgets
    searchSummonerBtn.grid(row = 0, column = 2, pady = 10, padx = 20)
  
    # infinite loop which can be terminated by keyboard 
    # # or mouse interrupt 
    mainloop()     
    
    
if __name__ == "__main__":

    run()
