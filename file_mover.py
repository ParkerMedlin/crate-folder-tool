import os
import shutil

# Set the paths to the directories containing the MP3 files, FLAC files, and empty subdirectories
mp3_dir = 'C:/Users/pmedlin/Dropbox/Music Songs'
flac_dir = 'C:/Users/pmedlin/Desktop/MUSICA'
empty_dir = 'C:/Users/pmedlin/Dropbox/Music2Songs'

# Get the list of subdirectories in the MP3 directory
mp3_subdirs = [f.name for f in os.scandir(mp3_dir) if f.is_dir()]

flac_files = [f.name for f in os.scandir(flac_dir) if f.is_file() and f.name.endswith('.flac')]


k=0

# Loop through the subdirectories and move the corresponding files
for subdir in mp3_subdirs:
    mp3_subdir_path = os.path.join(mp3_dir, subdir)
    empty_subdir_path = os.path.join(empty_dir, subdir)
    mp3_files = [f.name for f in os.scandir(mp3_subdir_path) if f.is_file() and f.name.endswith('.mp3')]
    if not os.path.exists(empty_subdir_path):
        print(f"Empty subdirectory '{empty_subdir_path}' does not exist. Skipping.")
        continue
    for flac_file in flac_files:
        for mp3_file in mp3_files:
            if flac_file.replace('.flac', '.mp3') in mp3_file:
                print(subdir)
                print(mp3_file)
                k=k+1
                print(str(k))
                file_path = os.path.join(flac_dir, flac_file)
                dest_file_path = os.path.join(empty_subdir_path, flac_file)
                # Move the file to the destination directory
                shutil.move(file_path, dest_file_path)
                print(f"Would move '{file_path}' to '{dest_file_path}'.")
