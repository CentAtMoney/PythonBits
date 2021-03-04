#!/usr/bin/python

import sys

def main(argv):
    if len(argv) != 3:
        print("Usage: " + argv[0] + "<file1> <file2>")
        return
    
    in_file1 = get_tokens(argv[1])
    in_file2 = get_tokens(argv[2])
    
    in_file1_not_in_file2 = in_file1 - in_file2

    in_file2_not_in_file1 = in_file2 - in_file1

    for token in in_file1_not_in_file2:
        print("< " + token)

    for token in in_file2_not_in_file1:
        print("> " + token)


    #spit everything into another file
    in_file1.update(in_file2)

    everything = list(in_file1)
    with open("everything", "w") as f:
        f.writelines("%s\n" % i for i in everything)

def get_tokens(filename, delim=None):
    tokens = set()

    #non newline delimiters not implemented
    if delim is not None:
        return tokens

    with open(filename) as f:
        for line in f:
            tokens.add(line)

    return tokens

if __name__ == "__main__":
    main(sys.argv)
