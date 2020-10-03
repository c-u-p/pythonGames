'''Modifications are : 
    1. decode feature is working in this code.
    Tips : You can copy the encrypted, decrypted or decoded the result
    and use the message with security
    and can share with your friend too!
'''
def encrypt(message, key):
    "Encrypt message with key."
    result = ''

    # Iterate letters in message and encrypt each individually.

    for letter in message:
        if letter.isalpha():

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            # The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            # TODO: Encrypt digits.
            result += letter

        else:
            result += letter

    return result

def decrypt(message, key):
    "Decrypt message with key."
    return encrypt(message, -key)

def decode(message):
    "Decode message without key."
    key1 = -19
    result1 = ''

    # Iterate letters in message and encrypt each individually.

    for letter1 in message:
        if letter1.isalpha():

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num1 = ord(letter1)

            if letter1.isupper():
                base1 = ord('A')
            elif letter1.islower():
                base1 = ord('a')

            # The encryption equation:

            num1 = (num1 - base1 + key1) % 26 + base1

            result1 += chr(num1)

        elif letter1.isdigit():

            # TODO: Encrypt digits.
            result1 += letter1

        else:
            result1 += letter1

    return result1

def get_key():
    "Get key from user."
    try:
        text = input('Enter a key (1 - 25): ')
        key = int(text)
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0
y='y'
while y=='y'or y=='Y':
    print('Do you wish to \n 1.encrypt \n 2.decrypt\n 3.decode \n a message?\n')
    print('Enter your choice : \n')
    choice = input()

    if choice == '1':
        phrase = input('Message: ')
        code = get_key()
        print('Encrypted message:', encrypt(phrase, code))
        print('Encoded successfully.....\n....\n...\n..\n.\n')
    elif choice == '2':
        phrase = input('Message: ')
        code = get_key()
        print('Decrypted message:', decrypt(phrase, code))
        print('Decrypted successfully.....\n....\n...\n..\n.\n')
    elif choice == '3':
        phrase = input('Message: ')
        print('Decoding message:')
        print ('Decoded message:', decode(phrase))
        print('Decoded successfully.....\n....\n...\n..\n.\n')
    else:
        print('Error: Unrecognized Command')
    print('Do you want to continue:Y or N')
    y=input()
