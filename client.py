import socket
import pyautogui
import webbrowser
import os
from appJar import gui

def receive_message():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    if data=="NUT":
        print("Running a command")
        webbrowser.open("https://www.youtube.com/watch?v=9bSGlMd1Y7Q")
        print("It's the nutshack")
    if data=="SHK":
        webbrowser.open("https://www.google.com/")
        pyautogui.sleep(5)
        pyautogui.typewrite("It's The Nutshack")
        pyautogui.press('enter')
    if data=="RES":
        print("Restarting")  
    if data=="SHU":
        os.system("shutdown /s /t 1")
        print("Powering Off")  
    if data=="SLE":
        print("Shuting Down")  
    conn.close()
    receive_message()
    
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
