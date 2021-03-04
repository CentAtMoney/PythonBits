#!/usr/bin/python
import sys

def main(argv):
    if len(argv) != 3:
        print("usage: " + argv[0] + " <x> <y>")
        return
    
    x = int(argv[1])
    y = int(argv[2])

    print(x / 8, y / 8)

if __name__ == "__main__":
    main(sys.argv)
