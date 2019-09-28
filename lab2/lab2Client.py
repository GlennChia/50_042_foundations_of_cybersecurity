"""
Lab2: Breaking Ciphers

GLENN CHIA 1003118
"""

from pwn import remote

# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    #print(challenge)
    # char_count = {}
    # for i in range(len(challenge)):
    #     if challenge[i] in char_count.keys():
    #         char_count[challenge[i]] += 1
    #     else:
    #         char_count[challenge[i]] = 1
    # print(char_count)
    # 
    ''' SORTING BASED ON COUNT
    [(50, 1292), (79, 750), (46, 559), (73, 466), (99, 454), (116, 448), (12, 357), 
    (75, 347), (124, 315), (62, 280), (69, 271), (45, 230), (59, 178), (9, 167), (32, 149), 
    (112, 146), (70, 142), (89, 115), (95, 105), (39, 102), (101, 95), (88, 91), (87, 76), 
    (60, 67), (86, 51), (115, 48), (51, 48), (117, 36), (118, 7), (82, 7), (123, 4), (102, 4), 
    (10, 1)]
    '''
    ''' CREATNG A MAPPING BASED ON THE SORTED ARRAY ABOVE
    {50: 1292, 79: 750, 46: 559, 73: 466, 99: 454, 116: 448, 12: 357, 75: 347, 124: 315, 62: 280, 
    69: 271, 45: 230, 59: 178, 9: 167, 32: 149, 112: 146, 70: 142, 89: 115, 95: 105, 39: 102, 101: 95, 
    88: 91, 87: 76, 60: 67, 86: 51, 115: 48, 51: 48, 117: 36, 118: 7, 82: 7, 123: 4, 102: 4, 10: 1 }
    '''
    mapping = {50: ' ', 79: 'e', 46: 't', 73: 'a', 99: 'o', 116: 'h', 12: 'r', 75: 'n',
        124: 'd', 62: 'i', 69: 's', 45: 'l', 59: 'w', 9: '\n', 32: 'g', 112: ',',
        70: 'u', 89: 'c', 95: 'm', 39: 'y', 101: 'f', 88: 'p', 87: '.', 60: 'b',
        86: 'k', 115: 'v', 51: '\"', 117: "-", 118: "'", 82: 'j', 123: 'q', 102: '?', 10: 'glenn'}

    solution = ''
    for i in range(len(challenge)):
        if challenge[i] in mapping.keys():
           solution += mapping[challenge[i]]
    # decrypt the challenge here
    solution = solution.encode('ascii')
    #solution = int(0).to_bytes(7408, 'big')
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # some all zero mask.
    # TODO: find the magic mask!
    original_message = 'Student ID 1000000 gets 0 points\n'.encode('ascii')
    edited_message = 'Student ID 1003118 gets 4 points\n'.encode('ascii')
    mask = XOR(original_message, edited_message)
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'points' in message:
        print(message)
    conn.close()


# def sol2():
#     conn = remote(URL, PORT)
#     message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
#     conn.sendline("2")  # select challenge 2

#     dontcare = conn.recvuntil(':')
#     challenge = conn.recvline()
#     # some all zero mask.
#     # TODO: find the magic mask!
#     # original_message = 'Student ID 1000000 gets 0 points\n'.encode('ascii')
#     # edited_message = 'Student ID 1003118 gets 4 points\n'.encode('ascii')
#     mask = b'\x00' * 33
#     marray = bytearray(mask)
#     marray[14] = 3
#     marray[15] = 1
#     marray[16] = 1
#     marray[17] = 8
#     marray[24] = 4
#     message = XOR(challenge, marray)
#     conn.send(message)
#     message = conn.recvline()
#     message = conn.recvline()
#     if b'points' in message:
#         print(message)
#     conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '34.239.117.115'
    PORT = 1337

    #sol1()
    sol2()
