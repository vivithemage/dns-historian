import socket

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


