#!/usr/bin/env python3

import argparse
import os
import qrcode
from PIL import Image, ImageColor  # ✅ Import Image for RGB conversion

# Define the output directory
OUTPUT_DIR = "output"


def generate_qr(data, filename="qr_code.png", box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates a QR code from the given data and saves it inside the 'output/' directory.

    Args:
        data (str): The text or URL to encode.
        filename (str): Output filename (default: "qr_code.png").
        box_size (int): Size of each QR code box (default: 10).
        border (int): Border thickness (default: 4).
        fill_color (str): QR code color (default: "black").
        back_color (str): Background color (default: "white").
    """
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Convert color names to RGB format
    try:
        fill_color = ImageColor.getrgb(fill_color)
        back_color = ImageColor.getrgb(back_color)
    except ValueError:
        print(f"⚠️ Warning: Invalid color name! Using default colors. ⚠️")
        fill_color = "black"
        back_color = "white"

    # Construct the full file path
    file_path = os.path.join(OUTPUT_DIR, filename)

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Convert QR image to RGB mode to support colors
    qr_img = qr.make_image(
        fill_color="black", back_color="white").convert("RGB")

    # Change fill and background color manually (fix for non-functional fill_color)
    pixels = qr_img.load()
    width, height = qr_img.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):  # Default black QR
                pixels[x, y] = fill_color  # Replace with custom fill color
            elif pixels[x, y] == (255, 255, 255):  # Default white background
                # Replace with custom background color
                pixels[x, y] = back_color

    # Save the modified image
    qr_img.save(file_path)
    print(f"✅ QR code saved as {file_path}")


def main():
    """Command-line interface to generate QR codes."""
    parser = argparse.ArgumentParser(
        description="Generate a QR code from text or a URL.")

    parser.add_argument(
        "data", type=str, help="The text or URL to encode in the QR code.")
    parser.add_argument("-o", "--output", type=str, default="qr_code.png",
                        help="Output file name (default: qr_code.png)")
    parser.add_argument("--box-size", type=int, default=10,
                        help="Size of QR code boxes (default: 10)")
    parser.add_argument("--border", type=int, default=4,
                        help="Size of border (default: 4)")
    parser.add_argument("--fill-color", type=str,
                        default="black", help="QR code color (default: black)")
    parser.add_argument("--back-color", type=str, default="white",
                        help="Background color (default: white)")

    args = parser.parse_args()

    generate_qr(args.data, args.output, args.box_size,
                args.border, args.fill_color, args.back_color)


if __name__ == "__main__":
    main()
