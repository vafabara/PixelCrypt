def encode():
    from PIL import Image
    import math
    import os

    while True:
        # User input
        text = input("Enter your text: ")
        location = input("Enter save location: ")
        file_name = input("Enter file name: ")

        if not file_name.endswith(".png"):
            file_name += ".png"

        # Convert text to Unicode code points.
        # RGB channels can store values from 0 to 255.
        ascii_codes = [ord(char) for char in text]

        if any(code > 255 for code in ascii_codes):
            print("Unsupported character!")
            print("Only characters with Unicode code points from 0 to 255 are supported.")
            continue

        pixel_count = math.ceil(len(ascii_codes) / 3)
        size = math.ceil(math.sqrt(pixel_count))

        image = Image.new("RGB", (size, size), (0, 0, 0))

        index = 0

        # Store up to 3 characters in each pixel:
        # Character 1 -> Red
        # Character 2 -> Green
        # Character 3 -> Blue
        for y in range(size):
            for x in range(size):
                if index < len(ascii_codes):
                    red = ascii_codes[index]
                    index += 1
                else:
                    red = 0

                if index < len(ascii_codes):
                    green = ascii_codes[index]
                    index += 1
                else:
                    green = 0

                if index < len(ascii_codes):
                    blue = ascii_codes[index]
                    index += 1
                else:
                    blue = 0

                image.putpixel((x, y), (red, green, blue))

        file_path = os.path.join(location, file_name)

        # For incorrect location
        if os.path.exists(location):
            image.save(file_path)
            image.show()

            capacity = size * size * 3

            print("\nEncryption completed.")
            print("Image Size:", size, "x", size)
            print("Maximum characters:", capacity)
            print("Characters used:", len(ascii_codes))
            print("Image saved in:", file_path)
        else:
            print("Invalid save location!")

        # Run Again
        again = input("\nDo you want to encrypt another text? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    encode()