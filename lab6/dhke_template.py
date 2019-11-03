#50.042 FCS Lab 6 template
#Year 2019

import primes_template 
import random

def dhke_setup(nb):
    # Generate an 80 bit prime number 
    # large_prime = primes_template.gen_prime_nbits(nb)
    # Instead of using the function, I will use Wolframalpha to save computation time
    # https://www.wolframalpha.com/ prime closest to 2^80
    p = 1208925819614629174706189
    # random.seed(30)
    # alpha = random.randint(2, p-2)
    # alpha is a generator of the group (But we don't have a group specified in the lab handout)
    # alpha = random.randint(2, 50) # Choose a small value to make computations fast
    alpha = 2
    return p, alpha

def gen_priv_key(p):
    # random.seed(1)
    # Comment out the one below to have a more varied private key but it will take longer to compute
    # a = random.randint(2, p-2)
    a = random.randint(2,10)
    # a = 15
    return a

def get_pub_key(alpha, a, p):
    return primes_template.square_multiply(alpha, a, p) # (alpha ** a ) % p

def get_shared_key(keypub,keypriv,p):
    return primes_template.square_multiply(keypub, keypriv, p) # (keypub ** keypriv) % p
    
if __name__=="__main__":
    p,alpha= dhke_setup(80)
    print ('Generate P and alpha:')
    print (f'P: {p}')
    print (f'alpha: {alpha}')
    print ('')
    a=gen_priv_key(p)
    b=gen_priv_key(p)
    print (f'My private key is: {a}')
    print (f'Test other private key is: {b}')
    print ('') 
    A=get_pub_key(alpha,a,p)
    B=get_pub_key(alpha,b,p)
    print (f'My public key is: {A}')
    print (f'Test other public key is: {B}')
    print ('')
    sharedKeyA=get_shared_key(B,a,p)
    sharedKeyB=get_shared_key(A,b,p)
    print (f'My shared key is: {sharedKeyA}')
    print (f'Test other shared key is: {sharedKeyB}')
    print (f'Length of key is {sharedKeyA.bit_length()} bits.')

