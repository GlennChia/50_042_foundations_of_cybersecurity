# string.printable checks if all characters in the string are in printable 
import sys
import argparse
import string

lowerKeyBoundary = 1
upperKeyBoundary = len(string.printable) - 1
lowerAsciiBoundary = 32
upperAsciiBoundary = 126
validAsciiCount = upperAsciiBoundary - lowerAsciiBoundary + 1

def encrypt(text, key):
    encryptedString = ''
    for i in range(len(text)):
        print("this is {} out of {}".format(i, len(text) - 1))
        # convert to Ascii (Ascii index is from 0 to 127 inclusive)
        asciiConversion = ord(text[i])
        # Valid range of characters is 32 (inclusive) to 126 (Inclusive)
        tempAsciiValue = asciiConversion + int(key)
        # Handle the case where it is out of range 
        if tempAsciiValue > upperAsciiBoundary:
            excessValue = tempAsciiValue - upperAsciiBoundary
            amountToIncrement = excessValue % validAsciiCount - 1
            tempAsciiValue = lowerAsciiBoundary + amountToIncrement
        encryptedString += chr(tempAsciiValue)
    return encryptedString


def decrypt(text, key):
    decryptedString = ''
    for i in range(len(text)):
        print("this is {} out of {}".format(i, len(text) - 1))
        # convert to Ascii (Ascii index is from 0 to 127 inclusive)
        asciiConversion = ord(text[i])
        # Valid range of characters is 32 (inclusive) to 126 (Inclusive)
        tempAsciiValue = asciiConversion - int(key)
        # Handle the case where it is out of range 
        if tempAsciiValue < lowerAsciiBoundary:
            excessValue = lowerAsciiBoundary - tempAsciiValue
            amountToDecrement = excessValue % validAsciiCount - 1
            tempAsciiValue = upperAsciiBoundary - amountToDecrement
        decryptedString += chr(tempAsciiValue)
    return decryptedString
    

def shiftCipher(filein, fileout, key, mode):
    # Validate the mode
    valid_modes = ['d', 'e', 'D', 'E']
    if mode not in valid_modes:
        raise Exception('Please enter a valid mode, you can choose d, e, D or E')
    # Validate the key that it is an integer # isinstance(<var>, int)
    if isinstance(key, int): #str.isdigit():
        # if 1 < key < len(string.printable) - 1:
        #     key = key % 25
        # else:
        #     raise Exception('The key length should be between 0 and len(string.printable) - 1')
        if key <= lowerKeyBoundary or key >= upperKeyBoundary - 1:
            raise Exception('The key length should be between 0 and len(string.printable) - 1')
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        switcher = {
                'd': decrypt,
                'D': decrypt,
                'e': encrypt,
                'E': encrypt
            }
        # Check the string format
        if all(c in string.printable for c in text):
            func = switcher.get(mode, lambda: "Invalid mode")
            finalString = func(text, key)  
            print(finalString)
    with open(fileout, mode="w", encoding='utf-8', newline='\n') as fout:
        fout.write(finalString)
    return finalString


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key',help='key')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key = args.key
    mode = args.mode

    shiftCipher(filein,fileout, key, mode)

    # all done