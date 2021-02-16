#!/usr/bin/env python
# Python 3.8: Walrus operation

with open("sample.txt") as handle:
    # Need to read once, then loop
    data = handle.read(64)
    while data:
        print(data)
        data = handle.read(64)
