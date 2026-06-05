from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            # Invert RGB values, keep alpha unchanged
            pixels[x, y] = (
                255 - r,
                255 - g,
                255 - b,
                a
            )

    img.save("encrypted.png")
    print("Image encrypted successfully!")
    print("Saved as encrypted.png")


def decrypt_image(image_path):
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            # Reverse inversion
            pixels[x, y] = (
                255 - r,
                255 - g,
                255 - b,
                a
            )

    img.save("decrypted.png")
    print("Image decrypted successfully!")
    print("Saved as decrypted.png")


print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice (1/2): ")
image_path = input("Enter image path: ")

if choice == "1":
    encrypt_image(image_path)
elif choice == "2":
    decrypt_image(image_path)
else:
    print("Invalid Choice")
    
