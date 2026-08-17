# PixelCrypt

PixelCrypt is a simple Python application that encodes text into an RGB image and decodes the image back into text.

## Version 2.1

PixelCrypt 2.1 improves the encoding system by using **all three RGB channels**, allowing up to **three characters to be stored in each pixel**.

This version also keeps the modern graphical interface built with **CustomTkinter**, providing a simple and user-friendly workflow for encoding and decoding.

## Features

* Encode text into an RGB image
* Decode text from an encoded image
* Store up to 3 characters per pixel using Red, Green, and Blue channels
* Approximately 3x the character capacity compared with the previous Red-only method
* Modern graphical user interface
* Encode / Decode mode switching
* Save images as PNG
* Custom save location
* Custom file name
* Automatic `.png` extension
* Image preview after encoding
* Decoded text preview
* File browser for selecting images and save locations
* Input validation and error handling

## GUI

The application provides a simple single-window interface with separate **Encode** and **Decode** modes.

### Encode

* Enter the text you want to encode
* Select the output folder
* Choose a file name
* Generate the encoded RGB image
* Preview the generated image directly in the application
* Store characters across the Red, Green, and Blue channels

### Decode

* Select an encoded image
* Read the Red, Green, and Blue channels in the same order used during encoding
* Decode the hidden text
* View the decoded text directly inside the application

## Project Structure

```text
PixelCrypt/
│
├── Main.py
├── GUI.py
├── rgb_encoder.py
├── rgb_decoder.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10+
* Pillow
* CustomTkinter

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Run

To launch the graphical interface:

```bash
python GUI.py
```

The terminal encoder and decoder can also be run directly:

```bash
python rgb_encoder.py
python rgb_decoder.py
```

## How It Works

PixelCrypt stores characters directly inside the three channels of an RGB image.

Each character is converted to its numeric character code and stored in one RGB channel:

```text
Character → Character Code → RGB Channel → Pixel
```

Each pixel can store up to three characters:

```text
Character 1 → Red
Character 2 → Green
Character 3 → Blue
```

For example, a pixel can contain:

```text
(R, G, B) = (72, 101, 108)
```

which represents:

```text
H → 72
e → 101
l → 108
```

During decoding, PixelCrypt reads the channels in the same order:

```text
Red → Green → Blue
```

and converts the stored values back into characters.

Because three channels are used instead of only the red channel, the new method can store up to **three characters per pixel**.

## Capacity

The required number of pixels is calculated from the number of characters:

```text
pixels = ceil(characters / 3)
```

The generated image is then created as a square large enough to contain those pixels.

For example:

```text
Text length: 300 characters
Required pixels: 100
Image size: 10 × 10
Capacity: 300 characters
```

## Limitations

The current encoding method stores character codes directly inside RGB channels, and each channel can store values from `0` to `255`.

Therefore, characters with Unicode code points greater than `255` cannot be encoded.

The current decoder also uses `0` as the marker for unused RGB channels in the final pixel.

## Version History

### Version 2.1

* Added RGB encoding using Red, Green, and Blue channels
* Increased storage capacity to up to 3 characters per pixel
* Updated terminal encoder
* Updated terminal decoder
* Updated GUI encoder
* Updated GUI decoder
* Updated capacity calculation
* Updated documentation

### Version 2.0

* Added CustomTkinter graphical interface
* Added image preview
* Added Encode / Decode mode switching
* Added file browser
* Added input validation
* Improved user experience
* Added decoded text display

### Version 1.0

* Initial terminal-based version
* Text encoding and decoding
* PNG image output
* Custom save location and file name

## License

This project is for educational and personal use.
