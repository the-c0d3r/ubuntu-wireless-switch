#!/usr/bin/env python

import os

def main():
    result = checkstate() 
    if result == 'up':
        disable()
    elif result == 'down':
        enable()

def enable():
    os.system('rfkill unblock wifi')

def disable():
    os.system('rfkill block wifi')

def checkstate():
    blocked = False
    os.system('rfkill list > tmp.result')
    fcontent = open('tmp.result').readlines()[1:2]
    for i in fcontent:
        if 'yes' in i.lower():
            blocked = True
    os.system('rm tmp.result')
    return 'up' if not blocked else 'down'

    
if __name__ == '__main__':
    main() 
