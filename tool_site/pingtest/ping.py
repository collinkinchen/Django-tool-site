#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess
import platform
import pandas as pd
import datetime 
import os

# This script works on UNIX machines #

def checkping(ip):
    return subprocess.call("ping -c 1 %s" % ip,shell=True)

def onePing(subnet,start,end):

    subnet = str(subnet.rpartition('.')[0])
    
    filename = subnet.replace(".","-") + "pingtest.txt"
    f = open(filename, 'w')
    liping = []
    for i in range(start,end):
        ipstr = subnet + "." +str(i)
        liping.append(ipstr)
    for ips in liping:
        with open(os.devnull,'w') as FNULL:
            try:
                subprocess.check_call("ping -c 1 %s" % ips,shell=True,stdout=FNULL)
                print("Ping %s successful" % ips)
            except subprocess.CalledProcessError:
                print("%s is unreachable" % ips)
                f.write("%s is unreachable \n" % ips)
                f.flush() 
                          
    f.close()


def main():
    # Check number of arguments
    if len(sys.argv) > 4: exit("not enough args. Expected IP range")
    # strip last value off IP range
    subnet = str(sys.argv[1].rpartition('.')[0])
    start  = int(sys.argv[2])
    try:
        end = int(sys.argv[3])
    except:
        end = 255
    print("Starting ping test on subnet: %s.0/24" % subnet)
    onePing(subnet,start,end)


if __name__ == '__main__':
    main()