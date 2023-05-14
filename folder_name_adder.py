import os
from mutagen.id3 import ID3, COMM
from mutagen.easyid3 import EasyID3
from mutagen import flac


# Here is the list of all the folders containing music
folder_paths = [
    r"C:/Users/pmedlin/Desktop",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/ambience",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/cafe_music",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/creepy_idm",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/dark_brooding",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/emotion_pretty",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/funk_bap",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/groovy_fun",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/hi_quality_filler",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/maximal_banger",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/meh_filler",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/moderate_subtle_banger",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/poppy",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/tasteless_maximal",
    # r"C:/Users/pmedlin/Dropbox/Music Songs/unclassified"
    ]

# for each folder path in the list
for folder_path in folder_paths:
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
                audio['comment'] = ('folder_name')
                audio.save()
        except Exception as e:
            print(f'error with {filename}: {str(e)}')
            continue
