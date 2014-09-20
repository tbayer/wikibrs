#!/usr/bin/python
# Quick-and-dirty script to add "<br />" tags to the end of every line
# of a text file, except those where MediaWiki will keep the line break
# anyway when parsing it as wikitext (e.g. after a line that starts
# with "*").
# By T. Bayer ([[user:HaeB]])
 
import os
import sys
import re
import codecs

usageexplanation = 'usage: wikibrs.py inputfile.txt outputfile.txt'


class wikibrs(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if not len(sys.argv) == 3:
    raise wikibrs(usageexplanation)


inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

inputfile = codecs.open(inputfilename, mode='r', encoding='utf-8')
outputfile = codecs.open(outputfilename, mode='w', encoding='utf-8')


line = ''
for nextline in inputfile:

    if re.match('[^*#;:=\n]', nextline):
        # don't append '<br />' if next line is empty,
        # or starts with *, #, ;, :, or =
        old = r'([^=])\n' # don't append '<br />' if line ends with a '='
        new = r'\1<br />\n'
        # see also https://en.wikipedia.org/wiki/User:Davidgothberg/The_br_tag
        line = re.sub(old, new, line)
        
    outputfile.write(line)
    
    line = nextline

inputfile.close()
outputfile.close()
