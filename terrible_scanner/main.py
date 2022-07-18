import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])
else:
    print('Invalid amount of args')
    print('Example: python main.py <ip>')
    sys.exit()

print('*' * 50)
print('target: {}'.format(sys[1]))
print('Time started: {}'.format(datetime.now()))
print('*' * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect({target, port})
        print('Checking port: {}'.format(port))
        if result == 0:
            print('Port {} is open'.format(port))
        s.close()
except KeyboardInterrupt:
    print('Scanning is stopped')
    sys.exit()
except socket.gaierror:
    print('Host couldn\'t be resolved')
    sys.exit()
except socket.error:
    print('Couldn\'t connect to server')
    sys.exit()