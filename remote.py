from appJar import gui
import socket

def receive_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)
    print("Waiting For A Connection")
    conn,addr = s.accept()
    print(f"Connection From{addr}")
    data = conn.recv(1024).decode()
    print(f"Received{data}")
    with open ('log.md','a') as f:
        f.write(f"From {addr}")
        f.write(f"\n")
        f.write(f"Message:{data}")
        f.write(f"\n")

def openfile(btn):
    if btn=="Close":
        print("BYE")
        app.stop()
    
app = gui("Remote",useTtk=True)
app.addImage("1",'images/radio.png')
app.addMessage("Waiting for an incoming connection")
app.addButtons(["Open Log","Close"],openfile)
app.go()