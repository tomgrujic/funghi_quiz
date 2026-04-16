import os
from PIL import Image


def compress_images(input_dir, output_dir, quality=80, resize=None):
    """
    Compress and optionally resize images, preserving folder structure.

    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory for compressed images.
        quality (int): JPEG quality (1-100). Default is 80.
        resize (tuple): Optional (width, height) to resize images. Default is None.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, file)

                # Create output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Open and process the image
                with Image.open(input_path) as img:
                    if resize:
                        img = img.resize(resize, Image.Resampling.LANCZOS)
                    img.save(output_path, optimize=True, quality=quality)

                print(f"Compressed: {input_path} -> {output_path}")


if __name__ == "__main__":
    # Define input and output directories
    input_directories = [
        "~/Downloads/Elenco specie fungine allegato 2a",
        "~/Downloads/Elenco specie fungine allegato 2b",
        "~/Downloads/Elenco specie fungine allegato 2c",
    ]

    output_directory = "compressed_images"

    # Compression settings
    jpeg_quality = 80  # Adjust quality (1-100)
    resize_dimensions = (
        800,
        800,  # Resize images to 800x800 for mobile suitability
    )

    for input_directory in input_directories:
        compress_images(
            os.path.expanduser(input_directory),
            output_directory,
            quality=jpeg_quality,
            resize=resize_dimensions,
        )
