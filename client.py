import socket
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
    if data=="CMD":
        print("Running a command")
    conn.close()
    receive_message()
    
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
