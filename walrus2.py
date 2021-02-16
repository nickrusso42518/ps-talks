#!/usr/bin/env python
# Python 3.8: Walrus operation

with open("sample.txt") as handle:
    # Like a "do-loop"; read and loop
    while data := handle.read(64):
        print(data)
