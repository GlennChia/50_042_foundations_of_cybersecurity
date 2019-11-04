# 50.042 FCS Lab 6 template
# Glenn Chia 1003118
# Year 2019

import primes_template 
import random

def dhke_setup(nb):
    '''
    Method 1: Using my own functions
    '''
    # Generate an 80 bit prime number 
    p = primes_template.gen_prime_nbits(nb)
    alpha = random.randint(2, p-2)
    '''
    Method 2: Using Wolfram Alpha's number
    '''
    # Instead of using the function, I will use Wolframalpha to save computation time
    # https://www.wolframalpha.com/ prime closest to 2^80
    # p = 1208925819614629174706189
    # alpha = random.randint(2, p-2)
    return p, alpha

def gen_priv_key(p):
    a = random.randint(2, p-2)
    return a

def get_pub_key(alpha, a, p):
    return primes_template.square_multiply(alpha, a, p) # (alpha ** a ) % p

def get_shared_key(keypub,keypriv,p):
    return primes_template.square_multiply(keypub, keypriv, p) # (keypub ** keypriv) % p
    
if __name__=="__main__":
    p,alpha= dhke_setup(80)
    print ('Generate P and alpha:')
    print ('P: {}'.format(p))
    print ('alpha: {}'.format(alpha))
    print ('')
    a=gen_priv_key(p)
    b=gen_priv_key(p)
    print ('My private key is: {}'.format(a))
    print ('Test other private key is: {}'.format(b))
    print ('') 
    A=get_pub_key(alpha,a,p)
    B=get_pub_key(alpha,b,p)
    print ('My public key is: {}'.format(A))
    print ('Test other public key is: {}'.format(B))
    print ('')
    sharedKeyA=get_shared_key(B,a,p)
    sharedKeyB=get_shared_key(A,b,p)
    print ('My shared key is: {}'.format(sharedKeyA))
    print ('Test other shared key is: {}'.format(sharedKeyB))
    print ('Length of key is {} bits.'.format(sharedKeyA.bit_length()))

