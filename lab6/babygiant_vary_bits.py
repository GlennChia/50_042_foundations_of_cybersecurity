# 50.042 FCS Lab 6 template
# Glenn Chia 1003118
# Year 2019

import math
import primes_template
import time
import random
import csv
from copy import deepcopy


def dhke_setup(nb):
    p = primes_template.gen_prime_nbits(nb)
    alpha = random.randint(2, p-2)
    return p, alpha

def gen_priv_key(p):
    a = random.randint(2, p-2)
    return a

def get_pub_key(alpha, a, p):
    return primes_template.square_multiply(alpha, a, p) # (alpha ** a ) % p

def get_shared_key(keypub,keypriv,p):
    return primes_template.square_multiply(keypub, keypriv, p) # (keypub ** keypriv) % p

def baby_step(alpha,beta,p,fname='baby_step.txt'):
    # Find the group order G
    g = p - 1 # since All elements of the eld except 0 form a multiplicative group with the group operation ×
    # Calculate m
    m = math.floor(math.sqrt(g))
    baby_step_result = {}
    for xb in range(m):
        result = (primes_template.square_multiply(alpha, xb, p) * beta)%p
        # result = (pow(alpha, xb, p) * beta)%p
        baby_step_result[xb] = result
    return baby_step_result


def giant_step(alpha,p,fname='giant_step.txt'):
    g = p - 1
    m = math.floor(math.sqrt(g))
    giant_step_result = {}
    for xg in range(m):
        result = primes_template.square_multiply(alpha, xg * m, p)
        # result = pow(alpha, xg * m, p)# alpha ** (xg * m)
        giant_step_result[xg] = result
    return giant_step_result


def baby_giant(alpha,beta,p):
    g = p - 1
    m = math.floor(math.sqrt(g))
    baby_step_result = baby_step(alpha, beta, p)
    giant_step_result = giant_step(alpha, p)
    for xb, baby_value in baby_step_result.items():
        for xg, giant_value in giant_step_result.items():
            if baby_value == giant_value:
                xb_final = xb
                xg_final = xg
    try:
        result = xg_final * m - xb_final
        return result
    except:
        return "none found"


if __name__=="__main__":
    completed_keys = []
    analysis = [] # Dictionaries added here 
    for i in range(2000):
        indiv_analysis = {}
        p, alpha = dhke_setup(30)
        a_priv=gen_priv_key(p)
        b_priv=gen_priv_key(p)
        A=get_pub_key(alpha,a_priv,p)
        B=get_pub_key(alpha,b_priv,p)
        sharedKey=get_shared_key(B,a_priv,p)
        sharedKeyLength = sharedKey.bit_length()
        print('shared key is {}'.format(sharedKey))
        print('shared key length is {}'.format(sharedKeyLength))
        if sharedKeyLength not in completed_keys: 
            start_time = time.time()
            # Break the shared key here 
            a=baby_giant(alpha,A,p)
            sharedKeyGuess=primes_template.square_multiply(B,a,p)
            # Record the time taken
            elapsed_time = time.time() - start_time
            print(elapsed_time)
            completed_keys.append(sharedKeyLength)
            indiv_analysis['key_length'] = sharedKeyLength
            indiv_analysis['time_taken'] = elapsed_time
            indiv_analysis['shared_key'] = sharedKey
            indiv_analysis['guessed_key'] = sharedKeyGuess
            indiv_analysis['p'] = p
            indiv_analysis['alpha'] = alpha
            indiv_analysis['private_a'] = a_priv
            indiv_analysis['private_b'] = b_priv
            indiv_analysis['public_a'] = A
            indiv_analysis['public_b'] = B
            indiv_analysis_copy = deepcopy(indiv_analysis)
            analysis.append(indiv_analysis_copy)
    print(analysis)
    csv_file = "./lab6/analysis.csv"
    csv_columns = ['key_length','time_taken','shared_key', 'guessed_key', 'p', 'alpha', 'private_a', 'private_b', 'public_a', 'public_b']
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in analysis:
                writer.writerow(data)
    except IOError:
        print("I/O error") 

    


