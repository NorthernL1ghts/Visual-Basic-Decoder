# VisualBasicExtensionDecoder

## Overview
The **VisualBasicExtensionDecoder** is a Python script that encodes and decodes text data. The data is encoded by reversing the string and then decoded by reversing it back to its original form. The encoded and decoded data is saved to files in the `../data/` and `../out/` directories, respectively.

This project is useful for situations where data needs to be encoded and decoded for processing or storage, following a simple algorithm for encoding (reversing the string).

## Features
- **Encoding**: The original data is encoded by reversing the string and saved to the `../data/encoded_file.txt` file.
- **Decoding**: The encoded data is read from the file, decoded (reversed), and saved to the `../out/decoded_file.txt` file.
- **Folder Management**: Automatically creates `../data/` and `../out/` directories if they don't exist.

## Prerequisites
- Python 3.x
- Basic understanding of Python file handling

## Setup & Installation
1. Clone this repository or download the Python script `VisualBasicExtensionDecoder.py`.
2. Ensure that you have Python 3.x installed on your machine.

## Usage
1. Open the script `VisualBasicExtensionDecoder.py` in a Python environment.
2. Modify the `originalData` variable in the script with the data you wish to encode and decode.
3. Run the script to generate the encoded and decoded files.

### Example:

```python
# Set the original data
originalData = "This is some sample data."
decoder.SetEncodedData(originalData)

# Encode the data and save it to the "../data/" folder
decoder.EncodeDataToFile('../data/encoded_file.txt')
print("Encoded data saved in '../data/encoded_file.txt'.")

# Decode the data from the "../data/" folder and save it to the "../out/" folder
decoder.DecodeFileToFile('../data/encoded_file.txt', '../out/decoded_file.txt')
print("Decoded data saved in '../out/decoded_file.txt'.")
