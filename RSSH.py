import paramiko
from appJar import gui

def create_server():
    # Get the server port number from the appJar text entry widget
    port = int(app.getEntry("Port"))

    # Create a new SSH server on the local machine
    ssh_server = paramiko.ServerInterface()
    ssh_server.start_server(server=paramiko.ServerStub())

    # Bind the server to the specified port number
    ssh_transport = paramiko.Transport(('localhost', port))
    ssh_transport.add_server_key(ssh_server.get_key())
    ssh_transport.start_server(server=ssh_server)

    # Save the server and transport objects in the appJar variable store
    app.saveGlobal("ssh_server", ssh_server)
    app.saveGlobal("ssh_transport", ssh_transport)

def open_website():
    # Get the URL to open from the appJar text entry widget
    url = app.getEntry("URL")

    # Get the SSH transport and start a new session
    ssh_transport = app.getGlobal("ssh_transport")
    ssh_channel = ssh_transport.accept(20)
    ssh_channel.invoke_shell()

    # Execute the command to open the website using the default web browser
    command = 'xdg-open {}'.format(url)
    ssh_channel.send(command + '\n')

    # Close the SSH channel and transport
    ssh_channel.close()
    ssh_transport.close()

# Create the appJar GUI
app = gui("Remote Website Opener")

# Create a new tab for the SSH server

app.addLabel("title", "Create SSH Server")
app.addLabelEntry("Port")
app.addButton("Create Server", create_server)
app.addLabel("title2", "Remote Website Opener")
app.addLabelEntry("URL")
app.addButton("Open Website", open_website)


# Start the GUI
app.go()
