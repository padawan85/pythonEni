import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers    import FTPHandler
from pyftpdlib.servers     import FTPServer

def main():

    dummy = DummyAuthorizer()
    dummy.add_user('parrot', 'pa$$', '.', perm='elradfmwMT')

    h = FTPHandler
    h.authorizer = dummy

    h.banner = "Bad FTP"

    addr = ('', 21)
    s = FTPServer(addr, h)

    s.max_cons = 256
    s.max_cons_per_ip = 5
    s.serve_forever()


main()
