#50.042 FCS Lab 6 template
# Year 2019

import random
def square_multiply(a,x,n):
    y = 1
    n_b = str(bin(x)).lstrip('0b')
    for i in range(len(n_b) - 1, -1, -1):
        y = (y ** 2) % n
        if n_b[i] == '1':
            y = (a * y) % n 
    return y

def miller_rabin(n, a):
    # n is the number to be tested
    # a is the number of rounds 
    # find r and d 
    n_sub_1 = n - 1 
    r = 0
    while n_sub_1 % 2 == 0:
        n_sub_1 //= 2
        r += 1
    d = n_sub_1
    # print(f'The value of d is {d}')
    # print(f'The value of r is {r}')
    for i in range(a):
        a = random.randint(2, n-2) 
        x = (a ** d) % n
        if x == 1 or x == n-1:
            continue
        state = 0
        for j in range(r-1):
            x = (x ** 2) % n
            if x == n-1:
                state = 1
                break
        if state == 1:
            continue
        return 'Probably not prime'
    return 'Probably prime'


def gen_prime_nbits(n):
    # Max value of an n bit integer is 2^n - 1
    # a = random.randint(2, 2**n -1)
    # 100 and 80 bits takes too long. Instead we will constrain it to 20 bits and pad it to 100 and 80 bits respectively
    a = random.randint(2, 2**20 -1)
    # Comment the code below if we really want 100 and 80 bits
    # a = random.randint(2, 2**n -1)
    while miller_rabin(a, 2) == 'Probably not prime':
        a = random.randint(2, 2**20 -1)
    # convert to binary representration  
    a_bin = str(bin(a)).lstrip('0b')
    padding = n - len(a_bin)
    pad_0 = '0' * padding
    a_bin = pad_0 + a_bin
    return a_bin # change this to a if we want the string representation

if __name__=="__main__":
    print(square_multiply(2,5,5))
    print ('Is 561 a prime?')
    print (miller_rabin(561,2))
    print ('Is 27 a prime?')
    print (miller_rabin(27,2))
    print ('Is 61 a prime?')
    print (miller_rabin(61,2))

    print ('Random number (100 bits):')
    print (gen_prime_nbits(100))
    print ('Random number (80 bits):')
    print (gen_prime_nbits(80))
