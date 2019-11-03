# 50.042 FCS Lab 6 template
# Glenn Chia 1003118
# Year 2019

import math
import primes_template


def baby_step(alpha,beta,p,fname='baby_step.txt'):
    # Find the group order G
    g = p - 1 # since All elements of the eld except 0 form a multiplicative group with the group operation ×
    # Calculate m
    m = math.floor(math.sqrt(g))
    baby_step_result = {}
    with open(fname, 'w') as fout:
        for xb in range(m):
            result = (primes_template.square_multiply(alpha, xb, p) * beta)%p
            # result = (pow(alpha, xb, p) * beta)%p
            fout.write(str(result) + '\n')
            baby_step_result[xb] = result
    return baby_step_result


def giant_step(alpha,p,fname='giant_step.txt'):
    g = p - 1
    m = math.floor(math.sqrt(g))
    giant_step_result = {}
    with open(fname, 'w') as fout:
        for xg in range(m):
            result = primes_template.square_multiply(alpha, xg * m, p)
            # result = pow(alpha, xg * m, p)# alpha ** (xg * m)
            fout.write(str(result) + '\n')
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
    """
    test 1
    My private key is:  264
    Test other private key is:  7265
    
    """
    p=17851  # We modulus by this
    alpha=17511  # This is a primitive element or generator in the group
    A=2945  # my public key
    B=11844  # other public key
    sharedkey=1671
    a=baby_giant(alpha,A,p)
    b=baby_giant(alpha,B,p)
    if b != "none found":
        guesskey1=primes_template.square_multiply(A,b,p)
        # guesskey1 = pow(A,b,p)
    if a != "none found":
        guesskey2=primes_template.square_multiply(B,a,p)
        guesskey2 = pow(B,a,p)
    try:
        print ('Guess key 1: {}'.format(guesskey1))
    except:
        pass
    try:
        print ('Guess key 2: {}'.format(guesskey2))
    except: 
        pass
    print ('Actual shared key: {}'.format(sharedkey))

