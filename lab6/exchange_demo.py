# 50.042 FCS Lab 6 Demo exchange
# Glenn Chia 1003118 with Tan Yi Xuan 1002887
# Year 2019

import primes_template 
import random
import ecb
import socket

HOST = '10.12.214.190'
PORT = 8888       

def dhke_setup(nb):
    p = 1208925819614629174706189
    alpha = 2
    return p, alpha

def gen_priv_key(p):
    return random.randint(2, p-2)

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
    print (f'My private key is: {a}')
    A=get_pub_key(alpha,a,p)
    print (f'My public key is: {A}')
    print ('')
    # Recieve partner's public key 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Send my public key
        s.sendall(A.to_bytes(10, 'big'))
        print('Sent public key')
        # Receive partner's public key
        B = int.from_bytes(s.recv(10), 'big')
        print('Received partner public key: {}'.format(B))
        # Send the encrypted message 
        sharedKeyA=get_shared_key(B,a,p)
        print ('Computed shared key is: {}'.format(sharedKeyA))
        print ('Length of shared key is: {} bits.'.format(sharedKeyA.bit_length()))
        encrypted_message= ecb.ecb(b'hello yx', sharedKeyA, 'e')
        print('Message encrypted: {}'.format(encrypted_message))
        # Get the length of the message to send 
        print('The length of the encrypted message is: {}'.format(len(encrypted_message)))
        s.send(len(encrypted_message).to_bytes(4, 'big'))
        print('Sent Message length')
        s.send(encrypted_message)
        print('Sent Encrypted message')
        # Receive the length of the message
        receive_length = int.from_bytes(s.recv(4), 'big')
        print('Received message length: {}'.format(receive_length))
        # Receive message
        receive_message = s.recv(receive_length)
        # Decrypt message
        decrypted_message = ecb.ecb(receive_message, sharedKeyA, 'd')
        print("The decrypted message is {}".format(str(decrypted_message, encoding='utf8')))
