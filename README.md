# Pixel Manipulation for Image Encryption

A Python-based image encryption and decryption tool that uses pixel manipulation techniques to secure images through RGB color inversion.

## 📋 Overview

This project implements a simple yet effective image encryption method by inverting the RGB values of each pixel in an image. While this method is suitable for educational purposes and basic obfuscation, it should not be used for highly sensitive data that requires military-grade encryption.

## 🎯 Features

- **Image Encryption**: Encrypts images by inverting RGB pixel values
- **Image Decryption**: Decrypts encrypted images by reversing the inversion process
- **Alpha Channel Preservation**: Maintains image transparency by keeping the alpha channel unchanged
- **User-Friendly Interface**: Simple command-line interface for easy operation
- **PNG Support**: Works with PNG and other image formats supported by PIL

## 🔧 Requirements

- Python 3.x
- PIL (Python Imaging Library) / Pillow

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/RashmiBansal-30/PRODIGY_CS_02.git
cd PRODIGY_CS_02
```

2. Install required dependencies:
```bash
pip install Pillow
```

## 🚀 Usage

Run the script:
```bash
python Pixel_Manipulation_for_Image_Encryption.py
```

### Interactive Menu
The script will prompt you with the following options:

```
1. Encrypt Image
2. Decrypt Image
Enter your choice (1/2): 
```

### Steps:
1. Enter your choice (1 for encryption or 2 for decryption)
2. Provide the path to your image file
3. The encrypted/decrypted image will be saved as:
   - `encrypted.png` (for encryption)
   - `decrypted.png` (for decryption)

### Example:
```
1. Encrypt Image
2. Decrypt Image
Enter your choice (1/2): 1
Enter image path: /path/to/your/image.png
Image encrypted successfully!
Saved as encrypted.png
```

## 🔐 How It Works

### Encryption Process:
- Opens the image in RGBA mode (Red, Green, Blue, Alpha)
- Iterates through each pixel in the image
- Inverts the RGB values using the formula: `new_value = 255 - old_value`
- Preserves the alpha channel (transparency)
- Saves the modified image

### Decryption Process:
- Since RGB inversion is a symmetric operation (applying it twice returns the original), decryption uses the same algorithm
- The inverted encrypted image is inverted again to recover the original

## 📝 Example

**Original Image**: 
- Pixel at (0,0): R=100, G=150, B=200, A=255

**After Encryption**:
- Pixel at (0,0): R=155, G=105, B=55, A=255

**After Decryption**:
- Pixel at (0,0): R=100, G=150, B=200, A=255 (Original recovered)

## ⚠️ Limitations

- **Not Cryptographically Secure**: This encryption method is for educational purposes only
- **Easily Reversible**: The encryption can be easily reversed by anyone with the script
- **Visual Manipulation**: The encrypted image looks inverted, making it obvious that encryption was applied
- **No Key System**: There is no key management system; the encryption is deterministic

## 💡 Educational Purpose

This project is part of the Prodigy CS 02 program and demonstrates:
- Basic image manipulation using PIL
- Pixel-level operations on images
- Understanding of RGB color models
- Simple symmetric encryption concepts

## 🔍 Supported Image Formats

The script supports all image formats supported by PIL/Pillow, including:
- PNG
- JPG/JPEG
- BMP
- GIF
- TIFF

## 📄 License

This project is open-source and available for educational and learning purposes.

## 👤 Author

[RashmiBansal-30](https://github.com/RashmiBansal-30)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements or suggestions.

---

**Note**: For actual image encryption in production environments, consider using established cryptographic libraries such as `cryptography` or `OpenSSL`.
