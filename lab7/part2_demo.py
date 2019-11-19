from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
import pyrsa_sq_mul
import socket

def generate_RSA(bits=1024):
    key = RSA.generate(bits)
    f_public = open('part3.pem.pub','wb')
    f_private = open('part3.pem.priv','wb')
    public_key = key.publickey().exportKey('PEM')
    private_key = key.exportKey('PEM')
    f_public.write(public_key)
    f_private.write(private_key)
    f_public.close()
    f_private.close()
    return private_key, public_key
    
def encrypt_RSA(public_key_file, message, state='sm'):
    key = open(public_key_file,'r').read()
    rsakey = RSA.importKey(key)
    if state == 'sm':
        if isinstance(message, int):
            byte_message_int = message
        else:
            byte_message_int = pyrsa_sq_mul.unpack_bigint(message)
        encrypt_byte_message_int = pyrsa_sq_mul.square_multiply(byte_message_int, rsakey.e, rsakey.n) 
        encrypt_byte_message_str = pyrsa_sq_mul.pack_bigint(encrypt_byte_message_int)
    elif state == 'part3':
        cipher_rsa = PKCS1_OAEP.new(rsakey)
        encrypt_byte_message_str = cipher_rsa.encrypt(message)
    return encrypt_byte_message_str

def decrypt_RSA(private_key_file, cipher, state='sm'):
    key = open(private_key_file,'r').read()
    rsakey = RSA.importKey(key)
    if state == 'sm':
        cipher_int = pyrsa_sq_mul.unpack_bigint(cipher)
        decrypted_byte_message_int = pyrsa_sq_mul.square_multiply(cipher_int, rsakey.d, rsakey.n) 
        decrypted_byte_message_str = pyrsa_sq_mul.pack_bigint(decrypted_byte_message_int)
    elif state == 'part3':
        cipher_rsa = PKCS1_OAEP.new(rsakey)
        decrypted_byte_message_str = cipher_rsa.decrypt(cipher)
    return decrypted_byte_message_str

def multiply_ciphers(cipher1, cipher2, public_key_file):
    cipher1 = pyrsa_sq_mul.unpack_bigint(cipher1)
    cipher2 = pyrsa_sq_mul.unpack_bigint(cipher2)
    key = open(public_key_file,'r').read()
    rsakey = RSA.importKey(key)
    mult_cipher_int = (cipher1 * cipher2) % rsakey.n
    mult_cipher_str = pyrsa_sq_mul.pack_bigint(mult_cipher_int)
    return mult_cipher_str

def sign_RSA(private_key_loc,data):
    key = open(private_key_loc, 'r').read()
    rsakey = RSA.importKey(key)
    message_hash = SHA256.new(data)
    # message_hash = SHA256.new()
    # message_hash.update(message)
    # message_hash_digest = message_hash.hexdigest() #.encode(encoding='utf-8')
    signature = PKCS1_PSS.new(rsakey).sign(message_hash)
    return signature, message_hash

def verify_sign(private_key_loc,sign,data):
    key = open(private_key_loc, 'r').read()
    rsakey = RSA.importKey(key)
    verifier = PKCS1_PSS.new(rsakey)
    try:
        verifier.verify(data, sign)
        return "The signature is authentic."
    except (ValueError, TypeError):
        return "The signature is not authentic."


if __name__=="__main__":
    '''Part II: Protocol Attack - Demo encryption and decryption of RSA.'''
    HOST = '10.12.214.190'
    PORT = 8888  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        '''
        For the first part I am Eve
        I will impersonate Alice and send x (message), s (signature)
        Bob already has Alice's public key, public key(e)
        '''
        print('I AM EVE FOR THIS ROUND\n')
        s = 100 #2019  # 111 11100011
        x = encrypt_RSA('mykey.pem.pub', s)
        print('Result of encryption with public key:\n{}\n'.format(x))
        print('Result of encryption with public key:\n{}\n'.format(b64encode(x)))
        # Send x length
        sock.send(len(x).to_bytes(4, 'big'))
        print('Sent x length: {}'.format(len(x)))
        # Send x
        sock.sendall(x)
        print('Sent new message x')
        # Send s
        sock.sendall(s.to_bytes(128, 'big'))
        print('Sent signature s: {}'.format(s))
        # Receive acknowledgement from partner 
        ## Receive the length of the message
        receive_length = int.from_bytes(sock.recv(4), 'big')
        print('Received message length: {}'.format(receive_length))
        ## Receive message
        receive_message = sock.recv(receive_length)
        if receive_message == b'OK':
            print('ATTACK SUCCESS')
        else:
            print('ATTACK FAILED\n')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        '''
        For the second part I am Bob
        I will receive x (message), s (signature)
        I already has Alice's public key, public key(e)
        '''
        print('I AM BOB FOR THIS ROUND\n')
        #x_receive_length = sock.recv(4)
        x_receive_length = int.from_bytes(sock.recv(4), 'big')
        print('Receive x length: {}'.format(x_receive_length))
        x_receive = sock.recv(x_receive_length)
        print('Result of encryption with public key received:\n{}\n'.format(b64encode(x_receive)))
        s_receive = sock.recv(128)
        s_receive_raw = int.from_bytes(s_receive, 'big')
        print('Received plain message:\n{}\n'.format(s_receive_raw))
        x_receive_prime = encrypt_RSA('mykey.pem.pub', s_receive_raw)
        print('x prime is:\n{}\n'.format(x_receive_prime))
        if x_receive == x_receive_prime:
            response_bob = 'OK'
            print('ATTACK SUCCESS')
        else:
            response_bob = 'ERR'
            print('ATTACK FAILED')
        sock.send(len(response_bob).to_bytes(4, 'big'))
        print('Sent length of response: {}'.format(len(response_bob).to_bytes(4, 'big')))
        sock.send(bytearray(response_bob, encoding='utf8'))
        print('Sent the response')
