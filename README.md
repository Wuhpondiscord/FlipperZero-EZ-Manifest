# FlipperZero EZ Manifest

FlipperZero EZ Manifest is a Python script, `EZ-Manifest.py`, that simplifies the creation of manifest files for subfolders containing animations. These manifest files describe the attributes of each animation subfolder.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows](#windows)
  - [macOS and Linux](#macos-and-linux)
- [Usage](#usage)
- [Default Manifest Folder](#default-manifest-folder)
- [ASCII Art](#ascii-art)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before using FlipperZero EZ Manifest, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

If you don't have `colorama` installed, the script will attempt to install it automatically.

## Installation

### Windows
1. **Download and install Python**: 
   - Visit the [official Python website](https://www.python.org/downloads/windows/).
   - Download the latest Python 3.x installer for Windows.
   - Run the installer and make sure to check the box that says "Add Python to PATH" during installation.

2. **Download the Script**:
   - Clone or download this repository by following these steps:
     - Click the green "Code" button at the top of this GitHub page.
     - Select "Download ZIP" to download the repository as a ZIP file.
     - Extract the ZIP file to a location of your choice.

3. **Open a Command Prompt or PowerShell window**.

4. **Navigate to the Project Directory**:
   - Use the `cd` command to change to the project directory where you extracted the ZIP file.

5. **Run the Script**:
   - Execute the script using the following command:
     ```
     python EZ-Manifest.py
     ```

### macOS and Linux
1. **Open a Terminal**.

2. **Check Python Installation**:
   - Make sure you have Python 3.x installed by running this command:
     ```
     python3 --version
     ```

   - If Python 3.x is not installed, you can usually install it using your system's package manager (e.g., `apt` for Ubuntu or `brew` for macOS).

3. **Download the Script**:
   - Clone or download this repository by following these steps:
     - Click the green "Code" button at the top of this GitHub page.
     - Copy the repository URL.
     - In your terminal, navigate to the directory where you want to save the script and run the following command:
     ```
     git clone https://github.com/Wuhpondiscord/FlipperZero-EZ-Manifest.git
     ```

4. **Navigate to the Project Directory**:
   - Use `cd FlipperZero-EZ-Manifest` to change to the project directory that was created when you cloned the repository.

5. **Run the Script**:
   - Execute the script using the following command:
     ```
     python3 EZ-Manifest.py
     ```

## Usage
1. When prompted, enter the path to the folder containing animations.

2. You can choose to use a default manifest folder or create a new one.

3. FlipperZero EZ Manifest will generate manifest files for all subfolders in the specified directory.

4. The manifest files will be saved in the manifest folder.

5. You can choose to generate another manifest or exit the program.

## Default Manifest Folder
FlipperZero EZ Manifest allows you to set a default manifest folder. If you have a default folder configured, the script will offer to use it every time you run the program.

To set a default manifest folder:
1. When prompted, create a new manifest folder.

2. The script will save the default manifest folder configuration in a `default_manifest.json` file.

## ASCII Art
ASCII Art found on [https://www.asciiart](https://www.asciiart.eu/) made by Normand Veilleux.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Your contributions are welcome!

## Help

If you encounter any common problems or issues, you can reach out for assistance.

Discord: wuhp

TikTok: @2vzk

Snapchat: samuel_dudhej

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

