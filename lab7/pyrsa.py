from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
import pyrsa_sq_mul

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
    '''Part I: RSA Without Padding'''
    print('Part I-------------')
    with open("message.txt") as f_message:
        message = f_message.read().encode()
    print('The message to encrypt is:\n{}\n'.format(message))

    cipher_rsa = encrypt_RSA('mykey.pem.pub', message)
    print('The cipher text after encryption is:\n{}\n'.format(b64encode(cipher_rsa)))

    decrypt_cipher = decrypt_RSA('mykey.pem.priv', cipher_rsa)
    print('The original message after decryption is:\n{}\n'.format(decrypt_cipher))

    message_hash = SHA256.new()
    message_hash.update(message)
    message_hash_digest = message_hash.hexdigest()
    print('The hash of the message is:\n{}\n'.format(message_hash_digest))

    encrypted_hash = encrypt_RSA('mykey.pem.pub', message_hash_digest.encode(encoding='utf-8'))
    print('The signed hash is:\n{}\n'.format(b64encode(encrypted_hash)))

    decrypt_hash = decrypt_RSA('mykey.pem.priv', encrypted_hash)
    print('The original message after decrypting the hash:\n {}\n'.format(decrypt_hash))

    '''Part II: Protocol Attack'''
    print('Part II-------------')
    plain_int = 100
    print('Encrypting: {}\n'.format(plain_int))

    cipher_int = encrypt_RSA('mykey.pem.pub', plain_int)
    print('Result:\n{}\n'.format(b64encode(cipher_int)))

    attack_num = 2
    cipher_attack = encrypt_RSA('mykey.pem.pub', attack_num)
    cipher_modified = multiply_ciphers(cipher_int, cipher_attack, 'mykey.pem.pub')
    print('Modified to: {}\n'.format(b64encode(cipher_modified)))

    decrypt_cipher_modified = decrypt_RSA('mykey.pem.priv', cipher_modified)
    print('Decrypted: {}'.format(pyrsa_sq_mul.unpack_bigint(decrypt_cipher_modified)))

    '''Part III: Implementing RSA with Padding (Local testing)'''
    print('Part III-------------')
    # part3_private_key, part3_public_key = generate_RSA()
    # print('The public key is:\n{}\n'.format(part3_public_key))
    # print('The private key is:\n{}\n'.format(part3_private_key))

    with open("mydata.txt", 'rb') as f_message_data:
        message_data = f_message_data.read()
    print('The message to encrypt is:\n{}\n'.format(message_data))

    cipher_pkcs = encrypt_RSA('part3.pem.pub', message_data, 'part3')
    print('The cipher text after encryption is:\n{}\n'.format(b64encode(cipher_pkcs)))

    decrypt_cipher_pkcs = decrypt_RSA('part3.pem.priv', cipher_pkcs, 'part3')
    print('The original message after decryption is:\n{}\n'.format(decrypt_cipher_pkcs))

    signed_hash, hashed_message = sign_RSA('part3.pem.priv', message_data)
    print('The signed hash is:\n{}\n'.format(signed_hash))

    print(verify_sign('part3.pem.pub', signed_hash, message_data))
