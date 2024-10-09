from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import timeit

# Keys
def generate_rsa_keypair(bits):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA
def rsa_encrypt(message, key):
    rsa_public_key = RSA.import_key(key)
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)
    encrypted_message = cipher_rsa.encrypt(message)
    return encrypted_message

# AES
def aes_encrypt(message, key):
    cipher_aes = AES.new(key, AES.MODE_EAX)
    nonce = cipher_aes.nonce
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)
    return key, nonce, ciphertext

# Funções de teste
def rsa_test(bits, message):
    
    start = timeit.default_timer()
    private_key, public_key = generate_rsa_keypair(bits)
    rsa_encrypt(message, public_key)
    encryption_time = timeit.default_timer() - start
    
    return encryption_time

def aes_test(bits, message):

    start = timeit.default_timer()
    key = get_random_bytes(bits//8)
    aes_encrypt(message, key)
    encryption_time = timeit.default_timer() - start
    
    return encryption_time
