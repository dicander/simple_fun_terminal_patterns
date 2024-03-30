# This program prints a random maze consisting of 45 degree unicode lines to the console

import random
import time

def print_maze():
    while True:
        if random.random()<0.5: # 50% chance of printing / or \ but the proper unicode 45 degree symbol
            print("\u2571", end="", flush=True)
        else:
            print("\u2572", end="", flush=True)
        time.sleep(0.001)

print_maze()