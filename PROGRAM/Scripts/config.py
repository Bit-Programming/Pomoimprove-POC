## Import the required modules
import sys, os


# This will give us the path of the application, the path of Chrome, the path of the Chrome user directory, and the path to the logo
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
    chrome_path = application_path + "\Chrome\chrome.exe"
    profile_path = application_path + "\Pomoprofile"
    logo_path = application_path + "\Images\Logo.png"
else:
    os.chdir("..")
    application_path = os.getcwd()
    if sys.platform == 'darwin':
        chrome_path = application_path + "/Pomoimprove/PROGRAM/Chrome/chrome.exe"
        profile_path = application_path + "/Pomoprofile"
        logo_path = application_path + "/Pomoimprove/PROGRAM/Images/Logo.png"
    elif sys.platform == 'win32':
        chrome_path = application_path + "\Pomoimprove\PROGRAM\Chrome\chrome.exe"
        profile_path = application_path + "\Pomoprofile"
        logo_path = application_path + "\Pomoimprove\PROGRAM\Images\Logo.png"
