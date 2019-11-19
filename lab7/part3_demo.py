from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
import pyrsa_sq_mul
import socket
import time

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
    message_hash = SHA256.new(data)
    try:
        verifier.verify(message_hash, sign)
        return "The signature is authentic."
    except (ValueError, TypeError):
        return "The signature is not authentic."


if __name__=="__main__":
    '''Part III: Implementing RSA with Padding - Demo RSA.'''
    HOST = '10.12.214.190'
    PORT = 8888  
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     sock.connect((HOST, PORT))
    #     '''
    #     For the first part I am sending my public key and then receiving a message to be decrypted
    #     '''
    #     print('############')
    #     print('FIRST PART FIRST SEGMENT: SEND PUBLIC KEY, RECEIVE MESSAGE AND CIPHER AND DECRYPT\n')
    #     print('############')
    #     # SEND THE PUBLIC KEY 
    #     f_public = open('part3.pem.pub','rb')
    #     my_public_key = f_public.read()
    #     f_public.close()
    #     print('My Public key sent is:\n{}\n'.format(my_public_key))
    #     sock.send(len(my_public_key).to_bytes(4, 'big'))
    #     print('Sent public key length: {}'.format(len(my_public_key)))
    #     sock.sendall(my_public_key)
    #     # RECEIVE THE MESSAGE AND DECRYPT
    #     receive_length_segment1 = int.from_bytes(sock.recv(4), 'big')
    #     print('Received message length: {}'.format(receive_length_segment1))
    #     receive_message_segment1 = sock.recv(receive_length_segment1)
    #     print('Received message:\n{}\n'.format(b64encode(receive_message_segment1)))
    #     decrypted_message_segment1 = decrypt_RSA('part3.pem.priv', receive_message_segment1, 'part3')
    #     print('Decrypted message is:\n{}\n'.format(decrypted_message_segment1))
    # time.sleep(1)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     sock.connect((HOST, PORT))
    #     print('############')
    #     print('FIRST PART SECOND SEGMENT: RECEIVE PUBLIC KEY, SEND MESSAGE AND CIPHER\n')
    #     print('############')
    #     # get public key message length from client
    #     pubkey_length = sock.recv(4)
    #     pubkey_length = int.from_bytes(pubkey_length, 'big')
    #     print("Received public key message length from client:", pubkey_length, 'bytes')
    #     # get public key from client
    #     pubkey = sock.recv(pubkey_length)
    #     with open('lab7_demo.pem.pub', 'wb') as pubkeyfile:
    #         pubkeyfile.write(pubkey)
    #     print("Received public key:\n{}\n".format(pubkey))
    #     # prepare message
    #     sent_mesage_segment1 = b'Hi, Glenn.'
    #     encrypted_message_segment1 = encrypt_RSA('lab7_demo.pem.pub', sent_mesage_segment1, 'part3')
    #     encrypted_message_segment1_length = len(encrypted_message_segment1).to_bytes(4, 'big')
    #     # send message length
    #     sock.send(encrypted_message_segment1_length)
    #     print('Sent encrypted message length: {}'.format(len(encrypted_message_segment1)))
    #     # send message
    #     sock.send(encrypted_message_segment1)
    #     print("Sent encrypted message: {}".format((encrypted_message_segment1)))
    #     print("Sent encrypted message: {}".format(b64encode(encrypted_message_segment1)))
    #     decrypted_message_segment2 = decrypt_RSA('mykey.pem.priv', encrypted_message_segment1, 'part3')
    #     print('Decrypted message is:\n{}\n'.format(decrypted_message_segment2))
    # time.sleep(1)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     sock.connect((HOST, PORT))
    #     '''
    #     For the second part I am sending my public key and message that is signed with my private key
    #     '''
    #     print('############')
    #     print('SECOND PART FIRST SEGMENT: SEND PUBLIC KEY, SEND MESSAGE, SEND SIGNED MESSAGE\n')
    #     print('############')
    #     # SEND THE PUBLIC KEY 
    #     f_public = open('part3.pem.pub','rb')
    #     my_public_key = f_public.read()
    #     f_public.close()
    #     print('My Public key sent is:\n{}\n'.format(my_public_key))
    #     sock.send(len(my_public_key).to_bytes(4, 'big'))
    #     print('Sent public key length: {}'.format(len(my_public_key)))
    #     sock.sendall(my_public_key)
    #     # SIGN THE MESSAGE
    #     with open("mydata.txt", 'rb') as f_message_data:
    #         message_data = f_message_data.read()
    #     signed_hash, hashed_message = sign_RSA('part3.pem.priv', message_data)
    #     print('The signed hash is:\n{}\n'.format(signed_hash))
    #     # SEND THE MESSAGE LENGTH and MESSAGE
    #     sock.send(len(message_data).to_bytes(4, 'big'))
    #     print('Message length_sent is: {}'.format(len(message_data)))
    #     sock.send(message_data)
    #     print('Message sent is: {}'.format(message_data))
    #     # SEND THE SIGNED MESSAGE
    #     sock.send(signed_hash)
    #     print('Raw Signed Message sent is:\n{}\n'.format(signed_hash))
    #     print('Signed Message sent is:\n{}\n'.format(b64encode(signed_hash)))
    #     print('JUST TO CHECK {}'.format(verify_sign('part3.pem.pub', signed_hash, message_data)))
    #     # Receive acknowledgement from partner 
    #     ## Receive the length of the message
    #     receive_length = int.from_bytes(sock.recv(4), 'big')
    #     print('Received message length: {}'.format(receive_length))
    #     ## Receive message
    #     receive_message = sock.recv(receive_length)
    #     if receive_message == b'OK':
    #         print('TRANSMISSION SUCCESS\n')
    #     else:
    #         print('TRANSMISSION FAILED\n')

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #     sock.connect((HOST, PORT))
    #     '''
    #     For the second part I am receiving my partner's public key and message that is signed with his private key
    #     '''
    #     print('############')
    #     print('SECOND PART SECOND SEGMENT: RECEIVE PUBLIC KEY, RECEIVE MESSAGE, RECEIVE SIGNED MESSAGE\n')
    #     print('############')
    #     # get public key message length from client
    #     pubkey_length = sock.recv(4)
    #     pubkey_length = int.from_bytes(pubkey_length, 'big')
    #     print("Received public key message length from client:", pubkey_length, 'bytes')
    #     # get public key from client
    #     pubkey = sock.recv(pubkey_length)
    #     with open('lab7_demo2.pem.pub', 'wb') as pubkeyfile:
    #         pubkeyfile.write(pubkey)
    #     print("Received public key:\n{}\n".format(pubkey))
    #     # Receive message length and message 
    #     message_partner_length = int.from_bytes(sock.recv(4), 'big')
    #     print("The length of my partner's message is: {}".format(message_partner_length))
    #     message_partner = sock.recv(message_partner_length)
    #     print('Received message:\n{}\n'.format(message_partner))
    #     # Receive signed message
    #     signed_message_partner = sock.recv(128)
    #     print('Received signed message:\n{}\n'.format(signed_message_partner))
    #     print('Received signed message:\n{}\n'.format(b64encode(signed_message_partner)))
    #     if verify_sign('lab7_demo2.pem.pub', signed_message_partner, message_partner) == "The signature is authentic.":
    #         response = 'OK'
    #         print('TRANSMISSION SUCCESS')
    #     else:
    #         response = 'ERR'
    #         print('TRANSMISSION FAILED')
    #     sock.send(len(response).to_bytes(4, 'big'))
    #     print('Sent length of response: {}'.format(len(response).to_bytes(4, 'big')))
    #     sock.send(bytearray(response, encoding='utf8'))
    #     print('Sent the response')

    # ##########
    # # Redo the protocol attack with the new RSA.
    # ##########
    print('#################')
    print('PROTOCOL ATTACK')
    print('#################')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        '''
        For the first part I am Eve
        I will impersonate Alice and send x (message), s (signature)
        Bob already has Alice's public key, public key(e)
        '''
        print('I AM EVE FOR THIS ROUND\n')
        s = 100 #2019  # 111 11100011
        x = encrypt_RSA('mykey.pem.pub', pyrsa_sq_mul.pack_bigint(s), 'part3')
        print('Result of encryption with public key:\n{}\n'.format(x))
        print('Result of encryption with public key:\n{}\n'.format(b64encode(x)))
        # Send x length
        sock.send(len(x).to_bytes(4, 'big'))
        print('Sent x length: {}'.format(len(x)))
        # Send x
        sock.sendall(x)
        print('Sent new message x')
        # Send s
        sock.send(len(pyrsa_sq_mul.pack_bigint(s)).to_bytes(4, 'big'))
        sock.sendall(pyrsa_sq_mul.pack_bigint(s))
        print('Sent signature s: {}'.format(s))
        # Receive acknowledgement from partner 
        ## Receive the length of the message
        receive_length = int.from_bytes(sock.recv(4), 'big')
        print('Received message length: {}'.format(receive_length))
        ## Receive message
        receive_message = sock.recv(receive_length)
        if receive_message == b'OK':
            print('ATTACK SUCCESS\n')
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
        s_receive_length = int.from_bytes(sock.recv(4), 'big')
        s_receive = sock.recv(s_receive_length)
        # s_receive_raw = int.from_bytes(s_receive, 'big')
        print('Received plain message:\n{}\n'.format(s_receive))
        x_receive_prime = encrypt_RSA('mykey.pem.pub', s_receive, 'part3')
        print('x prime is:\n{}\n'.format(x_receive_prime))
        if x_receive == x_receive_prime:
            response_bob = 'OK'
            print('ATTACK SUCCESS\n')
        else:
            response_bob = 'ERR'
            print('ATTACK FAILED\n')
        sock.send(len(response_bob).to_bytes(4, 'big'))
        print('Sent length of response: {}'.format(len(response_bob).to_bytes(4, 'big')))
        sock.send(bytearray(response_bob, encoding='utf8'))
        print('Sent the response')