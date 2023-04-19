import os
from mutagen.easyid3 import EasyID3

# Set the path to the folder containing the MP3 files
folder_path = r"C:\Users\pmedlin\Desktop\New Folder"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        # Load the metadata of the file
        audio = EasyID3(os.path.join(folder_path, filename))
        # Extract the artist and track information
        artist = audio["artist"][0]
        track = audio["title"][0]
        # Create a new filename with the desired format
        new_filename = f"{artist} - {track}.mp3"
        # Rename the file
        try:
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        except:
            print("error with " + str(artist) + str(track))
            continue