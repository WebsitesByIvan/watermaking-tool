# Image Watermarking Tool

This is a simple Python tool to watermark images using a PNG watermark.

## Instructions for running this program

 1. **Clone the Repository**
     Clone this repository to your local machine using Git:
     ```
     git clone https://github.com/WebsitesByIvan/watermaking-tool
     ```

 2. **Navigate to the project folder**
    ```
    cd watermark
    ```

 3.  **Set Up a Virtual Environment (Recommended)**

     It's good practice to create a virtual environment to isolate project dependencies:
     ```bash
     python -m venv env  # Create a virtual environment called 'venv'
     ```
     *   **On Windows:**
       ```bash
       env\Scripts\activate.bat  # Activate the virtual environment
       ```
     
 4.  **Install Dependencies**

     Install the required Python packages using `pip`:

     ```bash
     pip install -r requirements.txt
     ```

 5. **Run the script**
     Navigate to the `src` folder:
      ```bash
      cd src
      ```

     Then run the main script
     ```
     python main.py
     ```

 6.  **Select Images and Watermark**

     A file dialog will open. Select the images you want to watermark and the PNG watermark file.
     Watermarked files will be created in the same folder as the original images.

 ## Sample Assets

 The `assets/` folder contains some sample images and a watermark file you can use for testing.
 
 -   `sample1.jpg`
 -   `sample2.png`
 -   `watermark.png`

## Notes
- The output will be always a `.jpg` image with a `_watermarked` suffix. If you would like to have transparency in your output files modify the code as described in the comments section.

- Opacity and scale factor are hard-coded in the `main.py` file. If you would like to change these values, you will need to modify the variables in the code.

## Contributing

Feel free to contribute to this project with improvements and bug fixes.

## Author
Ivan Perez

## License

This project is licensed under the MIT License.
