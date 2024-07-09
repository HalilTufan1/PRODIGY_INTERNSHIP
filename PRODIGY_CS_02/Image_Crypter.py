from PIL import Image

def Crypter(source_path,output_path,mode,key):

    image = Image.open(source_path)
    pixels = image.load()

    width, height = image.size

    if mode == 'e':
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i,j]                           
                encrypted_pixel = (r ^ key,g ^ key,b ^ key)
                pixels[i,j] = encrypted_pixel
        image.save(output_path)   

    else:
        for i in range(width):
            for j in range(height):
                r,g,b = pixels[i,j]

                decrypted_pixel = (r ^ key,g ^ key,b ^ key)

                pixels[i,j] = decrypted_pixel
        image.save(output_path)


print()
print('*** IMAGE CRYPTER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt')
print()
user_input = input('e/d: ').lower()
print()
print('Enter the image decrypt key:')
print()
key = int(input('Key:'))
print('Enter the image source path:')
print()
input_path = input('Source Path:')
print('Enter the image output path:')
print()
output_path = input('Output Path:')


if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    Crypter(input_path, output_path, user_input,key)
    print('Image encrypted succesfully')

if user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    Crypter(input_path, output_path, user_input,key)
    print('Image decrypted succesfully')

    











