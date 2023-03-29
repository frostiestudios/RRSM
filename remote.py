from appJar import gui

app = gui("Remote","150x100",useTtk=True)
app.addImage("1",'images/globe.png')
app.addLabel('2',"REMOTE")
app.go()