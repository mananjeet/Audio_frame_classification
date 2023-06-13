import os

def get_wav_file_paths_with_zero(folder_path):
    wav_file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".wav") and "0" in file:
                file_path = os.path.join(root, file)
                wav_file_paths.append(file_path)
                break  # Exit the inner loop after finding the first file with 0

    return wav_file_paths

def write_to_txt(file_paths, output_file):
    with open(output_file, "w") as file:
        for file_path in file_paths:
            file.write(file_path + "\n")

# Example usage
folder_path = "headset"  # Replace with the actual folder path
output_file = "wav_file_paths.txt"  # Specify the output file name

wav_files = get_wav_file_paths_with_zero(folder_path)
write_to_txt(wav_files, output_file)
print("File paths written to", output_file)
