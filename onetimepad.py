import string
import random


def main_encrypt():
    data = input('Please type or paste the text, that you want to encrypt: \n')
    encrypted_data, key = encrypt(data)
    print('Encrypted data: \n' + encrypted_data)
    print('Key: \n' + key)


def main_decrypt():
    encrypted_data = input('Please type or paste the encrypted text: \n')
    key = input('Please type or paste the key: \n')
    decrypted_data = decrypt(encrypted_data, key)
    print('Decrypted data: \n' + decrypted_data)


def encrypt(data):
    key = ''.join(random.choice(string.ascii_lowercase) for x in range(len(data)))
    encrypted_data_list = list()

    for i in range(len(data)):
        encrypted_data_list.append(chr((ord(data[i]) + ord(key[i])) % 128))

    return (''.join(encrypted_data_list), key)


def decrypt(data, key):
    decrypted_data_list = list()

    for i in range(len(data)):
        decrypted_data_list.append(chr((ord(data[i]) - ord(key[i])) % 128))

    return ''.join(decrypted_data_list)


def onetimepad():
    print('\nChoose from the following options:: \n (1) encryption \n (2) Decryption \n (Anything else) Quit')
    choice = input()
    if choice == '1':
        main_encrypt()
        onetimepad()
    elif choice == '2':
        main_decrypt()
        onetimepad()
    else:
        print("Goodbye!")


print('Hello! I am a simple program demonstrating OTP encryption technique!')
onetimepad()
