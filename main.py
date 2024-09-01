from PIL import Image
import os

def compress_image(input_file_path, output_file_path, target_size_kb=1024):
    """
    Compresses an image to be under a target size in kilobytes.

    :param input_file_path: Path to the input image.
    :param output_file_path: Path to save the compressed image.
    :param target_size_kb: Target size in kilobytes. Default is 1024 KB (1MB).
    """
    # Open an image file
    with Image.open(input_file_path) as img:
        # If the image is not in RGB mode, convert it to RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Initialize the quality and step down the quality to meet the target size
        quality = 95
        while True:
            # Save the image to the output path with the current quality
            img.save(output_file_path, "JPEG", quality=quality)
            # Check the size of the image
            output_file_size_kb = os.path.getsize(output_file_path) / 1024

            # If the image is under the target size or quality is too low, stop
            if output_file_size_kb <= target_size_kb or quality <= 5:
                break

            # Otherwise, reduce the quality and try again
            quality -= 5

    print(f"Image saved to {output_file_path} with size {output_file_size_kb:.2f} KB")

# Example usage
input_path = "Profile Pic.JPG"
output_path = "OUTPUT.jpg"
compress_image(input_path, output_path)
