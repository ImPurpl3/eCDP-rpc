import pypresence
from pypresence import Presence
import tkinter as tk
import time
from random import randint
import sty
from sty import fg, RgbFg
from tkinter import *

#connecting to discord
client_id = '785245597279846442'
RPC = Presence(client_id)
RPC.connect()

#color varibles
fg.set_style('eCDP_Cyan', RgbFg(96, 136, 184))
cyan = fg.eCDP_Cyan + 'Thank You For Using My Rich Presence!' + fg.rs

fg.set_style('killConnect_Cyan', RgbFg(71, 180, 255))
cyanB = fg.killConnect_Cyan + 'Connection Will Close Shortly!'

fg.set_style('startUp', RgbFg(0, 88, 136))
start = fg.startUp + 'Starting Up!'

fg.set_style('statUp', RgbFg(232, 104, 168))
stat = fg.statUp + 'Status Updated!'

#setting the base rich presence
RPC.update(state="In Menus",details="Playing the eCrew Development Program" ,large_image="ecdp_ico", large_text="Playing eCDP", small_image="mcd_logo_disc", small_text="this really means nothing...")
print(start)

#defining some variables for the buttons
def chalRPC(): 
    RPC.update(details="Challanging the McDonald's" ,large_image="ecdp_ico", large_text="Playing eCDP", small_image="ok_disc", small_text="OK")
    print(stat)

def selfStudyRPC(): 
    RPC.update(details="Self Study" ,large_image="ecdp_ico", large_text="Playing eCDP", small_image="piss_bottle_disc", small_text="Piss Bottle uwu")
    print(stat)

def SOCGuideRPC():
    RPC.update(details="Reading the SOC Guide", large_image="ecdp_ico", large_text="Playing eCDP", small_image="soc_guide", small_text="SOC Guide")
    print(stat)

def selfCheckRPC():
    RPC.update(details="Doing a Self Check Test", large_image="ecdp_ico", large_text="Playing eCDP", small_image="ok_disc", small_text="OK")
    print(stat)

#defining the exit button's variables
def exitA():
    RPC.close()
    r.destroy()
    print(cyanB)
    time.sleep(12)
    print(cyan)
    time.sleep(2)
    exit()

#setting some important varibles
r = Tk() 
r.title('eCDP Rich Presence Dashboard')

#window icon
r.iconbitmap(r'C:\Users\Lenovo\Desktop\Stuff\eCDP Research\RPC\eCDP_rpc.ico')

#button variables
chal = tk.Button(r, text = 'Challenge the McDonalds', width = 50, command = chalRPC) 
selfStudy = tk.Button(r, text = 'Self Study', width = 50, command = selfStudyRPC)
SOCGuide = tk.Button(r, text = 'SOC Guide', width = 50, command = SOCGuideRPC)
selfCheck = tk.Button(r, text = 'Self Check', width = 50, command = selfCheckRPC)

exitB = tk.Button(r, text='Exit', width=50, command=exitA)

#puts buttons on screen
chal.pack()
selfStudy.pack()
SOCGuide.pack()
selfCheck.pack()

exitB.pack() 

#ending stuff
r.mainloop() 
while True:
    time.sleep(1)