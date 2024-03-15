import os
from mutagen.easyid3 import EasyID3
from mutagen import flac

# Set the path to the folder containing the MP3 files
folder_path = r"C:\Users\parkm\Desktop\ff"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    try:
        if filename.endswith(".mp3"):
            mp3_audio = EasyID3(os.path.join(folder_path, filename))
            artist = mp3_audio["artist"][0]
            title = mp3_audio["title"][0]
            new_filename = f"{artist} - {title}.mp3"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        elif filename.endswith(".flac"):
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
