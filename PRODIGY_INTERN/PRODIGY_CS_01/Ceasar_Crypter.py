letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


# def encrypt(plaintext, shift):
#     ciphertext= ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index + shift
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 ciphertext += letters[new_index]
#     return ciphertext

# def decrypt(ciphertext, shift):
#     plaintext= ''
#     for letter in ciphertext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index = index - shift
#                 if new_index < 0:
#                     new_index += num_letters
#                 plaintext += letters[new_index]
#     return plaintext

def decrypt_encrypt(text, mode, shift):
    result = ''
    if mode == 'd':
        shift = -shift
        
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + shift
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]       
    return result




print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt')
print()
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    shift = int(input('Enter the shift (1 through 26):'))
    text = input('Enter the text to encrypt: ')
    ciphertext = decrypt_encrypt(text, user_input, shift)
    print(f'CIPHERTEXT: {ciphertext}')

if user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    shift = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt_encrypt(text, user_input, shift)
    print(f'PLAINTEXT: {plaintext}')


