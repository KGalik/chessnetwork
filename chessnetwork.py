#!/usr/bin/python
# coding: utf-8
import urllib
import re

def main():
    uf = urllib.urlopen("https://en.wikipedia.org/wiki/Chess_World_Cup_2017") #opens wikipedia data
    webstring = uf.read() #reads data into string
    webstring = webstring.replace("½",".5") #replaces unicode fractions

    #includes some unicode characters found in names
    rankings = re.findall(r'>([\w -.łÉáčễọườơőí]+)</a>[, \w]*&#160;<span style="font-size:90%;">\(<abbr title="[\w ()]+">\w+</abbr>\)</span>, (\d+)', webstring, re.U)
    
if __name__ == '__main__':
    main()