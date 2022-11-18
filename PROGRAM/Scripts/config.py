import sys, os

# This will give us the path of the application, the path of Chrome, and the path to the logo
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
    chrome_path = application_path + "\Chrome\chrome.exe"
    logo_path = application_path + "\Images\Logo.png"
else:
    os.chdir("..")
    application_path = os.getcwd()
    chrome_path = application_path + "\Pomoimprove\PROGRAM\Chrome\chrome.exe"
    logo_path = application_path + "\Pomoimprove\PROGRAM\Images\Logo.png"