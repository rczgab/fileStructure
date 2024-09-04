import os

def list_files_recursively(folder_path):
    # Get the base name of the folder to use as the output file name
    folder_name = os.path.basename(os.path.normpath(folder_path))
    output_file = f"{folder_name}.txt"

    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # Get the full path of the file and write it to the output file
                file_path = os.path.join(root, filename)
                file.write(file_path + "\n")

    print(f"File names written to {output_file}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    list_files_recursively(folder_path)
