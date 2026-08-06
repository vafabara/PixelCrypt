def encode():
    
    from PIL import Image
    import math
    import os

    while True :

        # User input
        text = input("Enter your text: ")
        location = input("Enter save location: ")
        file_name = input("Enter file name: ")

        if not file_name.endswith(".png"):
            file_name += ".png"

        ascii_codes = []

        # Process
        for char in text:
            ascii_codes.append(ord(char))

        pixel_count = len(ascii_codes)

        size = math.ceil(math.sqrt(pixel_count))

        image = Image.new("RGB", (size, size), (0, 0, 0))

        index = 0

        for y in range(size):
            for x in range(size):

                if index < pixel_count:

                    red = ascii_codes[index]

                    image.putpixel((x, y), (red, 0, 0))

                    index += 1


        file_path = os.path.join(location, file_name)

        # For incorrect location
        if os.path.exists(location):
            image.save(file_path)
            image.show()

            capacity = size * size
            
            # Final print
            print("\nEncryption completed.")
            print("Image Size:", size, "x", size)
            print("Maximum characters:", capacity)
            print("Characters used:", pixel_count)
            print("Image saved in:", file_path)

        else:
            print("Invalid save location!")

        # Run Again
        again = input("\nDo you want to encrypt another text? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break