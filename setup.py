import os
from appJar import gui
def started(btn):
    if btn == "Setup":
        print("Starting Setup Sequence")
    if btn == "Cancel":
        print("Cancel")
app = gui("Setup Frostie Command Center")
app.addLabel("Welcome to Frostie Command Center")
app.addLabel("Lets Get Started")
app.addButtons(["Cancel","Setup"],started)
app.go()