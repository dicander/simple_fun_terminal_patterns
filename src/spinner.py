# This program shows a spinner until ctrl-c is pressed

import sys
import time

def spinner():
    while True:
        for i in '|/-\\':
            print(i, end="")
            time.sleep(0.1)
            print('\b', end="", flush=True)


try:
    spinner()
except KeyboardInterrupt:
    sys.exit()
