import rgb_encoder
import rgb_decoder

while True:
    print("\n -- PixelCrypt  --  ")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        rgb_encoder.encode()

    elif choice == "2":
        rgb_decoder.decode()

    elif choice == "3":
        break

    else:
        print("Invalid choice!")