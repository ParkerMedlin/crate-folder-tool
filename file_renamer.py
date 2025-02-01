import os
from mutagen.easyid3 import EasyID3
from mutagen import flac

# Set the path to the folder containing the MP3 files
folder_path = r"D:\Dropbox\Music2Songs\unclassified"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    try:
        if filename.endswith(".flac"):
            flac_audio = flac.FLAC(os.path.join(folder_path, filename))
            artist = flac_audio['artist'][0]
            title = flac_audio['title'][0]
            if artist in title:
                title = title.replace(artist + ' - ', '', 1)
            new_filename = f"{artist} - {title}.flac"
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(os.path.join(folder_path, filename), new_file_path)
    except Exception as e:
        print(f'error with {str(artist)} - {str(title)}: {str(e)}')
        continue
