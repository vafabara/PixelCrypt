def decode():
    from PIL import Image

    while True:
        # User Input
        image_path = input("Enter image path: ").strip().strip('"')

        try:
            image = Image.open(image_path).convert("RGB")
        except FileNotFoundError:
            print("Image not found!")
            continue
        except Exception as error:
            print("Unable to open image:", error)
            continue

        # Decode
        text = ""

        width, height = image.size
        finished = False

        for y in range(height):
            for x in range(width):
                red, green, blue = image.getpixel((x, y))

                # Read Red -> Green -> Blue.
                # A zero channel marks the unused part of the final pixel.
                for value in (red, green, blue):
                    if value == 0:
                        finished = True
                        break

                    text += chr(value)

                if finished:
                    break

            if finished:
                break

        # Result
        print("\nDecoded Text:")
        print(text)

        # Run Again
        again = input("\nDecode another image? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    decode()