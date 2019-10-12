#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

from present import *
import argparse

nokeybits=80
blocksize=64

def encrypt(f, key):
    valid = True
    output = []
    while valid:
        # Read in 8 bytes
        byte_in = f.read(8)
        if byte_in == b"":
            valid = False
        else:
            plain = int.from_bytes(byte_in, byteorder='big')
            encrypted = present(plain, key)
            output.append(encrypted)
    return output

def decrypt(f, key):
    valid = True
    output = []
    while valid:
        # Read in 8 bytes
        byte_in = f.read(8)
        if byte_in == b"":
            valid = False
        else:
            cipher = int.from_bytes(byte_in, byteorder='big')
            decrypted = present_inv(cipher, key)
            output.append(decrypted)
    return output


def ecb(infile, outfile, key, mode):
    with open(infile, 'br') as fin:
        switcher = { 'd': decrypt, 'D': decrypt, 'e': encrypt, 'E': encrypt }
        func = switcher.get(mode, lambda: "Invalid mode")
        baNew = func(fin, int(key))  
    with open(outfile, 'bw') as fout:
        for byte in baNew:
            fout.write((byte & (2**64-1)).to_bytes(8, byteorder='big'))
    return True

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode
    ecb(infile, outfile, keyfile, mode)



