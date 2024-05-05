# FlipperZero EZ Manifest

FlipperZero EZ Manifest is a Python script designed to simplify the creation of manifest files for subfolders containing animations. These manifest files describe the attributes of each animation subfolder.

## Prerequisites

Before using FlipperZero EZ Manifest, ensure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

If you don't have `colorama` installed, the script will attempt to install it automatically.

## Installation

1. **Download and Install Python**: 
   - Visit the [official Python website](https://www.python.org/downloads/).
   - Download and run the latest Python 3.x installer for your operating system.
   - During installation, make sure to check the box that says "Add Python to PATH."

2. **Download the Script**:
   - Clone or download the script from this repository.

3. **Install Dependencies**:
   - If Colorama is not installed, the script will attempt to install it automatically. However, you can manually install it using pip:
     ```
     pip install colorama
     ```

## Usage

1. **Run the Script**:
   - Navigate to the directory containing the script in your terminal or command prompt.
   - Run the script using the following command:
     ```
     python ez_manifest.py
     ```

2. **Follow the Prompts**:
   - When prompted, enter the path to the folder containing animations.
   - You can choose to use the default manifest folder or create a new one.
   - The script will generate manifest files for all subfolders in the specified directory.

3. **Review Manifest Files**:
   - Manifest files will be saved in the manifest folder.
   - Each manifest file describes the attributes of its corresponding animation subfolder.

4. **Generate Another Manifest (Optional)**:
   - You can choose to generate another manifest or exit the program.

## Configuration

- **Config File**:
  - FlipperZero EZ Manifest uses a `config.json` file to store configuration settings.
  - If the config file is not found, default values will be used.

- **Default Values**:
  - Default values for attributes such as min butthurt, max butthurt, min level, max level, and weight can be customized in the config file.

## Contributing

Contributions to FlipperZero EZ Manifest are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

