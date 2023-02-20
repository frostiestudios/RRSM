import socket
import json

with open('config.json') as f:
    config = json.load(f)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', config['port']))
s.listen(1)

conn, addr = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    
    data = data.decode().strip()
    
    if data.startswith("LINK:"):
        link = data[len("LINK:"):]
        # handle link
    elif data.startswith("COMMAND:"):
        command = data[len("COMMAND:"):]
        # handle command
    elif data.startswith("MESSAGE:"):
        message = data[len("MESSAGE:"):]
        # handle message
    else:
        # handle unknown data
    
conn.close()
