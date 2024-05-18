from PIL import Image
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def encrypt_image(image_path, key):
    
    original_image = Image.open(os.path.join(current_directory, image_path))
    width, height = original_image.size
    encrypted_image = Image.new("RGB", (width, height))
    
    for x in range(width):
        for y in range(height):
            pixel = original_image.getpixel((x, y))
            encrypted_pixel = tuple(p ^ key for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)
    
    return encrypted_image

def decrypt_image(encrypted_image_path, key):

    encrypted_image = Image.open(os.path.join(current_directory, encrypted_image_path))
    width, height = encrypted_image.size
    decrypted_image = Image.new("RGB", (width, height))
    
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple(p ^ key for p in encrypted_pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)
    
    return decrypted_image

image_path = "example_image.png"
key = 0b10101010  # Key in binary

encrypted_image = encrypt_image(image_path, key)
encrypted_image.save(os.path.join(current_directory, "encrypted_image.png"))

decrypted_image = decrypt_image("encrypted_image.png", key)
decrypted_image.save(os.path.join(current_directory, "decrypted_image.png"))
