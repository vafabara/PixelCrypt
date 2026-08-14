# PixelCrypt

PixelCrypt is a simple Python application that encodes text into an RGB image and decodes the image back into text.

## Version 2.0

PixelCrypt 2.0 introduces a modern graphical interface built with **CustomTkinter**, replacing the original terminal-based workflow with a simple and user-friendly GUI.

## Features

* Encode text into an RGB image
* Decode text from an encoded image
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
* Generate the encoded image
* Preview the generated image directly in the application

### Decode

* Select an encoded image
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

## How It Works

PixelCrypt stores each character of the input text inside the **red channel** of an RGB image.

Each character is converted to its numeric character code and stored in a pixel:

```text
Character → Character Code → Red Channel → RGB Pixel
```

During decoding, PixelCrypt reads the red channel of each pixel and converts the stored values back into characters.

## Limitations

The current encoding method stores character codes directly inside an RGB channel, so characters with code points greater than `255` cannot be encoded.

## Version History

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
