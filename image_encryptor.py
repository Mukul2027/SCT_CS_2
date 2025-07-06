from PIL import Image

def encrypt_image(image_path, output_path, operation="invert"):
    image = Image.open(image_path)
    pixels = image.load()
    
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if operation == "invert":
                pixels[x, y] = (255 - r, 255 - g, 255 - b)
            elif operation == "add":
                shift = 50
                pixels[x, y] = (
                    (r + shift) % 256,
                    (g + shift) % 256,
                    (b + shift) % 256
                )
            elif operation == "swap":
                pixels[x, y] = (b, g, r)

    image.save(output_path)
    print(f"Image saved as: {output_path}")

def decrypt_image(image_path, output_path, operation="invert"):
    encrypt_image(image_path, output_path, operation)

if __name__ == "__main__":
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option: ")

    path = input("Enter path to image (e.g. sample.png): ")
    output = input("Enter output image name (e.g. encrypted.png): ")
    op = input("Choose operation (invert / add / swap): ")

    if choice == "1":
        encrypt_image(path, output, op)
    elif choice == "2":
        decrypt_image(path, output, op)
    else:
        print("Invalid choice.")
