import os
import shutil
import sys


def copy_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for dir in dirs:
            dest_subdirectory = os.path.join(
                destination_dir, os.path.relpath(os.path.join(root, dir), source_dir))
            os.makedirs(dest_subdirectory, exist_ok=True)
            print(f"Directory '{dir}' created in '{dest_subdirectory}'")
            copy_files(os.path.join(root, dir), dest_subdirectory)
        for file in files:
            if source_dir != root:
                continue
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]
            dest_subdirectory = os.path.join(
                destination_dir, file_extension[1:])
            os.makedirs(dest_subdirectory, exist_ok=True)
            try:
                shutil.copy2(file_path, dest_subdirectory)
                print(f"File '{file}' copied to '{dest_subdirectory}'")
            except Exception as e:
                print(f"Error copying file '{file}': {str(e)}")


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)
    source_dir = sys.argv[1]

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    if len(sys.argv) < 3:
        destination_dir = 'dist'
    else:
        destination_dir = sys.argv[2]
    os.makedirs(destination_dir, exist_ok=True)

    copy_files(source_dir, destination_dir)


if __name__ == "__main__":
    main()
