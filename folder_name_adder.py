import os
from mutagen.id3 import ID3, COMM
from mutagen.easyid3 import EasyID3
from mutagen import flac

parent_folder_path = r"C:/Users/parkm/Dropbox/Music2Songs"
folder_paths = [os.path.join(parent_folder_path, d) for d in os.listdir(parent_folder_path) if os.path.isdir(os.path.join(parent_folder_path, d))]

# Here is the list of all the folders containing music
folder_paths_to_ignore = [
    r"C:/Users/parkm/Dropbox/Music2Songs/unclassified"
    ]

# for each folder path in the list
for folder_path in folder_paths:
    if folder_path not in folder_paths_to_ignore:
        # Get the name of the folder
        folder_name = os.path.basename(folder_path)

        # Loop through all files in this folder
        for filename in os.listdir(folder_path):
            try:
                if filename.endswith(".mp3"):
                    audio = ID3(os.path.join(folder_path, filename))
                    # print(audio.keys()) # prints all the dict keys
                    # Set a custom TXXX frame to store the folder name
                    if folder_name not in audio["COMM::XXX"][0]:
                        audio.add(COMM(encoding=3, text=folder_name))
                    # Save the changes to the metadata
                    audio.save()
                elif filename.endswith(".flac"):
                    audio = flac.FLAC(os.path.join(folder_path, filename))

                    audio['comment'] = (folder_name)
                    audio.save()
            except Exception as e:
                print(f'error with {filename}: {str(e)}')
                continue
