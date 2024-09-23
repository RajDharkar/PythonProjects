import os
from pathlib import Path

directoryList = {
    "EXE_Folder": ["exe"],
    "PICTURES": ["png", "jpeg", "gif", "jpg", "heif"],
    "VIDEOS": ["mov", "mp4", "mpg", "mkv", "mpeg", "vmv"],
    "ZIP": ["zip", "iso", "tar", "gz", "rz", "7z", "dmg", "rar"],
    "MUSIC": ["mp3", "msv", "wav", "wma"],
    "PDF": ["pdf", "html", "html5", "htm", "xhtml"]
}

# Mapping the File Format to the Directory
File_Format_Dictionary = {
    final_file_format: directory
    for directory, file_format_stored in directoryList.items()
    for final_file_format in file_format_stored
}

def organizer():
    for file in os.scandir():
        if file.is_dir():
            continue
        file_path = Path(file)
        final_file_format = file_path.suffix.lower()[1:]  

        # Check if the file's format is in the mapping dictionary
        if final_file_format in File_Format_Dictionary:
            directory_name = File_Format_Dictionary[final_file_format]
            directory_path = Path(directory_name)
            os.makedirs(directory_path, exist_ok=True)  # Create the directory if it doesn't exist
            os.rename(file_path, directory_path / file_path.name)  # Use / for path joining

    # Iterate again to check for empty directories
    for dir in os.scandir():
        if dir.is_dir():
            try:
                os.rmdir(dir)  # Remove the empty directory
            except OSError:  # Catch any errors when trying to remove a directory
                print(f"Could not remove directory: {dir.name}")

        else:
            # Move files that do not match any directory to 'Other_Folder'
            other_folder = Path("Other_Folder")
            os.makedirs(other_folder, exist_ok=True)  # Create 'Other_Folder' if it doesn't exist
            try:
                os.rename(dir.path, other_folder / dir.name)  # Move the file
            except ValueError as e:
                print(f"Failed to move {dir.name}: {e}") #error handling

if __name__ == "__main__":
    organizer()
