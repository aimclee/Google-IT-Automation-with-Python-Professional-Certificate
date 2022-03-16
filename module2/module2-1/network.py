import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True

def gethostbyname(localhost):
    return localhost

def check_connectivity():
    request = requests.get("http://www.google.com")
    if request.status_code == 200:
        return True