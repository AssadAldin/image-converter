import os
from PIL import Image

def convert_images_to_webp(input_folder, output_folder):
    """
    Convert all .jpg images in the input folder to .webp format and save them in the output folder.

    Args:
        input_folder (str): Path to the folder containing .jpg images.
        output_folder (str): Path to the folder where .webp images will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".jpg"):  # Check if the file is a .jpg
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.rsplit('.', 1)[0] + ".webp")  # Change extension to .webp

            try:
                # Open the image and convert it to webp
                with Image.open(input_path) as img:
                    img.save(output_path, "WEBP")
                print(f"Converted: {file_name} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {file_name}: {e}")

if __name__ == "__main__":
    # Specify the input and output folders
    input_folder = "path/to/your/input/folder"
    output_folder = "path/to/your/output/folder"

    convert_images_to_webp(input_folder, output_folder)
