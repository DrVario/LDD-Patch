import os
from pathlib import Path

print("Locating Files")
print(os.getenv('APPDATA'))
appdata = os.getenv('APPDATA')
os.chdir(appdata)
os.chdir('..')
os.chdir(r"Local\Temp\WZSE0.TMP")
print(os.getcwd())
while True:
    try:
        os.remove("install_flash_player_active_x.exe")
        print("Removing Old Flash Player Version 10")
        break
    except (RuntimeError):
        print("File could not be found! Please close lego Digital Designer and try again.") 
    os.rename("OpenGLChecker.exe", "install_flash_player_active_x.exe")
    print("All Done! Go ahead and finish the install now!")

