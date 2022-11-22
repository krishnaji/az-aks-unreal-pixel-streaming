import asyncio
import sys
import socket
import os
import re
import redis
import connections

r = redis.Redis(host="redis", port=6379, db=0)

# get hostname
hostname = socket.gethostname()

def playerConnected(line):
    # "20:41:05.442 player 101 (::ffff:127.0.0.1) connected"
    playerConnectedPattern = re.compile(r'(\d{2}:\d{2}:\d{2}.\d{3}) player (\d{3}) (\(\:\:ffff\:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)) connected')
    match = playerConnectedPattern.search(line)
    if match:
        connections.playerConnected(r)
        print("Player connected: {} to {} ".format(match.group(2), hostname))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

def playerDisconnected(line):
    # "20:42:19.994 player 101 connection closed: 1005"
    playerDisconnectedPattern = re.compile(r'(\d{2}:\d{2}:\d{2}.\d{3}) player (\d{3}) connection closed: (\d{4})')
    match = playerDisconnectedPattern.search(line)
    if match:
        connections.playerDisconnected(r)
        print("Player disconnected: {} from {} ".format(match.group(2), hostname))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

# tail a log file
async def tail(filename):
    print('Tailing file: {}'.format(filename))
    with open(filename) as f:
        f.seek(0, 2)
        while True:
            line = await loop.run_in_executor(None, f.readline)
            if not line:
                await asyncio.sleep(0.1)
                continue
            playerConnected(line)
            playerDisconnected(line)
            await asyncio.sleep(0.1)
   
# main method
if __name__ == '__main__':
    log_path = os.environ.get('LOG_DIR')
    print('Log path: {}'.format(log_path))
    # get latest log file from the directory
    import glob
    import time
    while True:
        list_of_files = glob.glob(log_path + '/*') 
        if list_of_files:
            latest_file = max(list_of_files, key=os.path.getctime)
            print(latest_file)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(tail(latest_file))
        else:
            print("No log file found")
            # wait for 5 seconds
            time.sleep(5)





