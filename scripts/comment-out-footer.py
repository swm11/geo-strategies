#!/usr/bin/env python3

import sys

files = sys.argv[1:]
for fn in files:
    fin = open(fn, 'r')
    out = ""
    for x in fin:
        if('<div id="footer" class="footer">' in x):
            x.rstrip()
            out = out+'<!-- '+x+' -->\n'
        else:
            out = out+x
    fin.close()
    fout = open(fn, 'w')
    fout.write(out)
    fout.close()
