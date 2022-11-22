# redis connection

def playerConnected(r):
    r.incr('CONNECTIONS')

def playerDisconnected(r):
    r.decr('CONNECTIONS')

