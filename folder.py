import os
import shutil

def merge_files_into_folders(source_directory, destination_directory):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Get all the files in the source directory
    files = os.listdir(source_directory)

    # Create a dictionary to store files with the same name in the first 6 places
    file_dict = {}

    # Iterate over each file
    for filename in files:
        source_file = os.path.join(source_directory, filename)

        # Skip directories
        if os.path.isdir(source_file):
            continue

        # Extract the first 7 characters of the file name
        name_key = filename[:7]

        # Remove '.' if it exists in the name key
        if '.' in name_key:
            name_key = name_key.replace('.', '')

        # Add the file to the dictionary based on the name key
        if name_key in file_dict:
            file_dict[name_key].append(source_file)
        else:
            file_dict[name_key] = [source_file]

    # Iterate over the file dictionary
    for name_key, file_list in file_dict.items():
        # Skip if there is only one file with the name key
        if len(file_list) == 1:
            continue

        # Create the destination folder with the name key
        destination_folder = os.path.join(destination_directory, name_key)
        os.makedirs(destination_folder, exist_ok=True)

        # Copy each file to the destination folder
        for source_file in file_list:
            filename = os.path.basename(source_file)
            destination_file = os.path.join(destination_folder, filename)
            shutil.copy(source_file, destination_file)

            print(f"Copied file '{filename}' to folder '{name_key}'")

# Example usage
source_directory = "words"
destination_directory = "XML"
os.makedirs(destination_directory, exist_ok=True)

merge_files_into_folders(source_directory, destination_directory)
