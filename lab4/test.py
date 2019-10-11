round22 = 0xff00ffff000000  # 64 bits
round22Correct = 3729037392057742272#
pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
       4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
       8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
       12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

def sBoxLayer(state):
    mask = 0xf
    output = 0
    for i in range(16):
        sboxOut = sbox[state & mask]
        output = output | (sboxOut<<(i*4))
        state = state >> 4
    return output

def pLayer(state):
    # use the pmt array for the mapping
    output = 0
    for i in range(64):
        shifted_value = ((state >> i) & 0x01) << pmt[i]
        output = output | shifted_value
    return output

print(pLayer(round22))