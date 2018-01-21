import os 
from colorama import Fore, Back, Style
#MEMORY FLODDER THAT GIVES YOU CHANCE>>>>>>>>YOU CAN ACT

mspaint = lambda: os.system('mspaint')
continueExec=True
evil_level=2
while(continueExec==True):
    give_chance= input(Fore.GREEN+Back.RED+Style.DIM +"Enter the Password")
    if(give_chance=="600613"):
        continueExec=False
    else:
        for x in range(1,evil_level):
            mspaint()
        evil_level+=1
        print(Fore.RED+Back.GREEN+"SORRY DUDE.....EVIL LEVEL JUST INCREASED TO ",evil_level-1)
                  
        
