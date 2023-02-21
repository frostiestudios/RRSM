import os
import webbrowser
from appJar import gui 

def join(btn):
    print("Joining Server")
    webbrowser.open_new_tab("https://acstuff.ru/s/q:race/online/join?ip=70.187.129.123&httpPort=8081")

app=gui("AC Server Joiner")
app.addButton("Join",join)
app.go()