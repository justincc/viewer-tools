#!/usr/bin/python

import argparse
import datetime
import string

############
### MAIN ###
############
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument(
    '--date',
    help = "Date in the format <y>-<m>-<d> for which to produce log.  For example, 2014-09-09.  If omitted then is today's date.",
    default = datetime.date.today().strftime("%Y-%m-%d"),
    metavar = "<date>")

parser.add_argument(
    'outputPath',
    help = "Output path for the generated chat log.",
    metavar = "<output-path>")

parser.add_argument(
    'logPath', 
    help = "Path to the chat log file.", 
    metavar = "<chat-log-path>",
    nargs = '+')

opt = parser.parse_args()

#print "Date: %s" % opt.date
#print "LogPath: %s" % opt.logPath

date = opt.date.translate(string.maketrans("-", "/"))
linesFound = 0

with open(opt.outputPath, 'w') as o:
    
    o.write('''<pre style="white-space: pre-wrap; 
white-space: -moz-pre-wrap;
white-space: -pre-wrap;
white-space: -o-pre-wrap; 
word-wrap: break-word">''')

    for path in opt.logPath:
        with open(path) as f:
            for line in f:
                if line.startswith("[%s" % date):
                    o.write(line)
                    linesFound += 1
                    
    o.write("</pre>")
                    
print "Found %s lines for %s" % (linesFound, date)                    