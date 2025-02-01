import os
from mutagen.id3 import ID3, COMM
from mutagen.easyid3 import EasyID3
from mutagen import flac

parent_folder_path = r"D:\Dropbox\Music2Songs\unclassifiedD:\Dropbox\Music2Songs\unclassified"
# folder_paths = [os.path.join(parent_folder_path, d) for d in os.listdir(parent_folder_path) if os.path.isdir(os.path.join(parent_folder_path, d))]

folder_paths = [
    r"D:\Dropbox\Music2Songs\unclassified"
]

# Here is the list of all the folders containing music
folder_paths_to_ignore = [
    # r"D:\Dropbox\Music2Songs\unclassified"
    ]

# for each folder path in the list
for folder_path in folder_paths:
    if folder_path not in folder_paths_to_ignore:
        # Get the name of the folder
        folder_name = os.path.basename(folder_path)

        # Loop through all files in this folder
        for filename in os.listdir(folder_path):
            try:
                # Use ffmpeg to convert the mp3 file to flac
                if filename.endswith(".mp3"):
                    input_file = os.path.join(folder_path, filename)
                    output_file = os.path.join(folder_path, filename.replace(".mp3", ".flac"))
                    os.system(f'ffmpeg -i "{input_file}" "{output_file}"')
                #     old_mp3_folder = r"C:/Users/parkm/Desktop/old mp3s"
                #     if not os.path.exists(old_mp3_folder):
                #         os.makedirs(old_mp3_folder)
                #     if filename.endswith(".mp3"):
                #         old_mp3_path = os.path.join(old_mp3_folder, filename)
                #         os.rename(os.path.join(folder_path, filename), old_mp3_path)
            except Exception as e:
                print(f'error with {filename}: {str(e)}')
                continue