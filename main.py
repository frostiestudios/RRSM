from appJar import gui
import socket
import json
with open('clients.json') as f:
    data = json.load(f)

ip_addresses = [pc['ip_address'] for pc in data['pcs']]    
def send_content(btn):
    ip_address = app.getOptionBox("IP Address")
    message = app.getEntry("Message")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 12345))
    s.sendall(message.encode())
def newclient(btn):
    name = app.getEntry("PC NAME")
    ipad = app.getEntry("IP Address")
    new_pc = {"name:": name, "ip_address": ipad}
    data["pcs"].append(new_pc)
    with open('clients.json', 'w') as file:
        json.dump(data, file, indent=2)
    app.setEntry("PC NAME", "")
    app.setEntry("IP Address", "")

app = gui()
app.addLabelEntry("Message")
app.addButton("Send", send_content)
app.addOptionBox("IP Address", ip_addresses)

app.startLabelFrame("Add A New Client")
app.addLabelEntry("PC NAME")
app.addLabelEntry("IP Address")
app.addButton("Enter",newclient)
app.stopLabelFrame()
app.go()