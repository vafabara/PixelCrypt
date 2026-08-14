def decode():

    from PIL import Image

    while True:

        # User Input
        image_path = input("Enter image path: ").strip().strip('"')

        try:
            image = Image.open(image_path)

        except FileNotFoundError:
            print("Image not found!")
            continue

        # Decode
        text = ""

        width, height = image.size

        for y in range(height):
            for x in range(width):

                red, green, blue = image.getpixel((x, y))

                if red == 0:
                    break

                text += chr(red)

            else:
                continue

            break

        # Result
        print("\nDecoded Text:")
        print(text)

        # Run Again
        again = input("\nDecode another image? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break

decode()