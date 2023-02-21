import webbrowser
import pyautogui
webbrowser.open("https://www.google.com/")
pyautogui.sleep(5)
pyautogui.typewrite("It's The Nutshack")
pyautogui.press('enter')