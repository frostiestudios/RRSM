from appJar import gui
import os
import webbrowser
import subprocess
import threading
import pyautogui
print("Starting Initial Loading")
print("LOG1")
print("LOG2")
print("LOG3")
print("LOG4")
print("History Avail Below")
print("______________")
#Unicode Numbers
PLAY= 	"\u23F5"
def fair(btn):
    print("opening")
    webbrowser.open_new_tab("https://fareharbor.com/flightdeck1/dashboard/bookings/grid/2023-02-25/")
def xampp(btn):
    if btn=="XAMPPStart":
        print("opening XAMPP")
        os.startfile("C:/XAMPP/xampp-control.exe")
        print("xampp")
        os.startfile("C:/XAMPP/apache_start.bat")
        print("apache")
        os.startfile("C:/XAMPP/mysql_start.bat")
        print("mysql")
        app.infoBox("Success", "Apache and MySQL servers started!")
def lc(btn):
    print("Lounge Control")
    if btn=="LCOpen":
        print("Lounge Control Is Running")
        os.startfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
    if btn=="LCStop":
        print("Lounge Control Is Closed")
        os.stopfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
def lcs(btn):
    if btn=="Remote Launcher":
        webbrowser.open_new("https://192.168.1.12:6001/ACLauncherControl")
        print("RemLauncher")
    if btn=="Leaderboard Control":
        webbrowser.open_new("https://192.168.1.12:6001/RemoteViewSettings")
        print("Remote View Leaderboard")
def ms(btn):    
    print("MultiServer")
    if btn=="MSOpen":
        os.startfile("C:\LoungeControl\LoungeControl-ACMultiServer\LC-AC-MultiServer.exe")
def text():
    "text"
def debug():
    print("debugging")
    
tools = ["Start", "Stop"]
app = gui("Rogue Command Center",useTtk=True)
app.addLabel("Title","Command Center",0,1)
app.startLabelFrame("XAMPP",1,1)

app.addButtons(["XAMPPStart","XAMPPStop"],xampp)
app.stopLabelFrame()

app.startLabelFrame("Lounge Control",1,2)
app.addButtons(["LCOpen","LCStop"],lc)
app.stopLabelFrame()

app.startLabelFrame("MultiServer",1,3)
app.addButtons(["MSOpen","MSStop"],ms)
app.stopLabelFrame()

app.startLabelFrame("Lounge Control Settigns",2,1,2)
app.addButtons(["Remote Launcher","Leaderboard Control"],lcs)
app.stopLabelFrame()

app.startLabelFrame("FairHarbor Settings",2,3)
app.addButtons(["Open Fair Harbor"],fair)
app.stopLabelFrame()

app.startLabelFrame("Debug",3,1,3)
app.addImage("I5","images/help.png")
app.stopLabelFrame()

app.startLabelFrame("Sigma",5,1)

app.stopLabelFrame()
app.go()
