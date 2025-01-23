# Image converter
Here's a Python script that converts all .jpg images in a folder to .webp format using the Pillow library:

## First create your venv
    python3 -m venv myenv
### Activate the Virtual Environment
### On Linux/MacOS:

    source myenv/bin/activate

### On Windows (Command Prompt):

    myenv\Scripts\activate

### Run this command:

    myenv\Scripts\activate

### On Windows (PowerShell):

    .\myenv\Scripts\activate

### Confirm Activation
Once activated, the name of the virtual environment (e.g., myenv) will appear in the terminal prompt, like this:

    (myenv) $

You are now inside the virtual environment, and any Python packages installed will be scoped to this environment.

## Install the Required Library
Make sure you have the Pillow library installed. If not, install it using pip:

    pip install pillow

## How to Use the Script
1-Replace path/to/your/input/folder with the path to the folder containing your .jpg images.

2-Replace path/to/your/output/folder with the path to the folder where the .webp images should be saved.

3-Run the script:

        python convert_to_webp.py

## Output
1-All .jpg images in the input folder will be converted to .webp format and saved in the specified output folder.

2-The script will print the status of each conversion.