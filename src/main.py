from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def watermark_image(image_path, watermark_path, output_path="watermarked_image.jpg", opacity=0, watermark_scale=1):
    """
    Watermarks an image with a PNG image.

    Args:
        image_path (str): Path to the input image.
        watermark_path (str): Path to the PNG watermark image.
        output_path (str, optional): Path to save the watermarked image. Defaults to "watermarked_image.jpg".
        opacity (int, optional): Opacity of the watermark (0-255). Defaults to 128.
        watermark_scale (float, optional): Scale factor for the watermark (0-1). Defaults to 0.30.
    """

    try:
        # 1. Open the Main Image
        image = Image.open(image_path).convert("RGBA")
        image_width, image_height = image.size

        # 2. Open the Watermark Image
        watermark = Image.open(watermark_path).convert("RGBA")
        watermark_width, watermark_height = watermark.size


        # 3. Resize the Watermark
        new_watermark_width = int(image_width * watermark_scale)
        new_watermark_height = int(watermark_height * (new_watermark_width/watermark_width)) # Maintain aspect ratio

        watermark = watermark.resize((new_watermark_width, new_watermark_height))


        # 4. Create a Watermark Mask
        watermark_mask = watermark.split()[3]

        # 5. Calculate Watermark Position
        x = (image_width - new_watermark_width) // 2 # Center horizontally
        y = (image_height - new_watermark_height) // 2 # Center vertically


        # 6. Apply Opacity and Paste
        watermark = watermark.convert("RGBA")
        watermark = Image.blend(watermark, Image.new("RGBA", watermark.size, (0, 0, 0, 0)), (opacity/255))
        image.paste(watermark, (x,y), mask=watermark_mask)

        # 7. Convert to RGB and Save the Watermarked Image
        image = image.convert("RGB") # Convert before saving as JPEG
        image.save(output_path)
        print(f"Image watermarked successfully. Saved to: {output_path}")


    except FileNotFoundError:
        print(f"Error: Image or Watermark file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def select_images():
    """Opens a file dialog to select multiple images and a watermark file."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not image_paths:
        messagebox.showinfo("Info", "No images selected.")
        return None, None

    watermark_path = filedialog.askopenfilename(title="Select Watermark", filetypes=[("PNG files", "*.png")])
    if not watermark_path:
      messagebox.showinfo("Info", "No watermark selected.")
      return None, None

    return image_paths, watermark_path


def process_images(image_paths, watermark_path):
    """Processes a list of image paths with the specified watermark"""

    if image_paths and watermark_path:
        for image_path in image_paths:
            try:
               output_path = os.path.splitext(image_path)[0] + "_watermarked.jpg"
               watermark_image(image_path, watermark_path, output_path)
            except Exception as e:
                 print(f"Error processing image {image_path}: {e}")


if __name__ == "__main__":
     image_paths, watermark_path = select_images()
     process_images(image_paths, watermark_path)


