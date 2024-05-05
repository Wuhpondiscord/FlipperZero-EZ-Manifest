import os
import json
import subprocess

try:
    import colorama
except ImportError:
    print("Colorama library is not installed. Installing...")
    subprocess.call(["pip", "install", "colorama"])

import colorama
from colorama import Fore, init

init(autoreset=True)

def create_manifest_entry(name):
    min_butthurt = 0
    max_butthurt = 1000
    min_level = 1
    max_level = 1000
    weight = 8

    manifest_entry = f"""
Name: {name}
Min butthurt: {min_butthurt}
Max butthurt: {max_butthurt}
Min level: {min_level}
Max level: {max_level}
Weight: {weight}
"""
    return manifest_entry

def generate_manifest_file(manifest_folder, base_filename):
    manifest_filename = f"{base_filename}.txt"
    counter = 1

    while os.path.exists(os.path.join(manifest_folder, manifest_filename)):
        manifest_filename = f"{base_filename}{counter}.txt"
        counter += 1

    return os.path.join(manifest_folder, manifest_filename)

def create_manifest_folder():
    manifest_folder = input(f"{Fore.CYAN}Enter the path to the manifest folder: ")

    try:
        if not os.path.exists(manifest_folder):
            os.mkdir(manifest_folder)
        return manifest_folder
    except Exception as e:
        print(f"{Fore.MAGENTA}Error creating the manifest folder: {e}")
        return None

def find_subfolder_names(folder):
    try:
        subfolder_names = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
        return subfolder_names
    except Exception as e:
        print(f"{Fore.MAGENTA}Error while searching for subfolders: {e}")
        return []

def generate_manifest_for_subfolders(animation_folder, manifest_folder):
    try:
        manifest_base_filename = "manifestmaker"
        manifest_path = generate_manifest_file(manifest_folder, manifest_base_filename)

        manifest = f"{Fore.MAGENTA}\n\nFiletype: Flipper Animation Manifest\nVersion: 1\n"

        subfolder_names = find_subfolder_names(animation_folder)

        if not subfolder_names:
            print(f"{Fore.CYAN}No subfolders found in the specified directory.")
            return

        print(f"{Fore.MAGENTA}Creating manifest files for all subfolders in '{animation_folder}'...")

        for subfolder_name in subfolder_names:
            entry = create_manifest_entry(subfolder_name)
            manifest += entry

        with open(manifest_path, "w") as file:
            file.write(manifest)

        print(f"{Fore.CYAN}Manifest file '{os.path.basename(manifest_path)}' created in '{manifest_folder}'.")
    except Exception as e:
        print(f"{Fore.MAGENTA}An error occurred while generating the manifest: {e}")

def save_default_manifest_folder(default_manifest_folder):
    try:
        with open("default_manifest.json", "w") as file:
            json.dump({"default_manifest_folder": default_manifest_folder}, file)
    except Exception as e:
        print(f"{Fore.MAGENTA}Error while saving the default manifest folder: {e}")

def load_default_manifest_folder():
    try:
        if os.path.exists("default_manifest.json"):
            with open("default_manifest.json", "r") as file:
                data = json.load(file)
                return data.get("default_manifest_folder")
        return None
    except Exception as e:
        print(f"{Fore.MAGENTA}Error while loading the default manifest folder: {e}")
        return None

def display_ascii_art():
    print(f"{Fore.MAGENTA}a,  8a")
    print(f" {Fore.MAGENTA} `8, `8){Fore.MAGENTA}                            ,adPPRg,")
    print(f"  {Fore.MAGENTA}8)  ]8                        ,ad888888888b")
    print(f" {Fore.MAGENTA} ,8' ,8'                    ,gPPR888888888888")
    print(f"{Fore.MAGENTA},8' ,8'                 ,ad8\"\"   `Y888888888P")
    print(f"{Fore.MAGENTA}8)  8)              ,ad8\"\"        (8888888\"\"")
    print(f"{Fore.MAGENTA}8,  8,          ,ad8\"\"            d888\"\"")
    print(f"{Fore.MAGENTA}`8, `8,     ,ad8\"\"            ,ad8\"\"")
    print(f" {Fore.MAGENTA} `8, `{Fore.MAGENTA},ad8\"\"            ,ad8\"\"")
    print(f"{Fore.MAGENTA}    ,gPPR8b           ,ad8\"\"")
    print(f"{Fore.MAGENTA}   dP:::::Yb      ,ad8\"\"")
    print(f"{Fore.MAGENTA}   8):::::(8  ,ad8\"\"     {Fore.CYAN}by discord @wuhp")
    print(f"{Fore.MAGENTA}   Yb:;;;:d888\"\"            {Fore.CYAN}tiktok @2vzk")
    print(f"{Fore.MAGENTA}    \"8ggg8P\"                
    print()

def main():
    while True:
        try:
            default_manifest_folder = load_default_manifest_folder()
            animation_folder = input(f"{Fore.CYAN}Enter the path to the folder containing animations: ")

            if default_manifest_folder:
                use_default = input(f"{Fore.CYAN}Use default manifest folder '{default_manifest_folder}'? (Y/N): ").strip().lower()
                if use_default == 'y':
                    manifest_folder = default_manifest_folder
                else:
                    manifest_folder = create_manifest_folder()
            else:
                manifest_folder = create_manifest_folder()
                save_default_manifest_folder(manifest_folder)

            display_ascii_art()
            generate_manifest_for_subfolders(animation_folder, manifest_folder)

            again = input(f"{Fore.CYAN}Do you want to generate another manifest? (Y/N): ").strip().lower()
            if again != 'y':
                break
        except Exception as e:
            print(f"{Fore.MAGENTA}An error occurred: {e}")

if __name__ == "__main__":
    main()
