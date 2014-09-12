#!/usr/bin/python

import argparse

############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument(
    'logPath', 
    help = "Path to the chat log file.", 
    metavar = "chat-log-path",
    nargs='*')

opt = parser.parse_args()

for path in opt.logPath:
    with open(path) as f:
        for line in f:
            print line