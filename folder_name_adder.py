import os
# from mutagen.id3 import ID3, COMM
# from mutagen.easyid3 import EasyID3
from mutagen import flac

parent_folder_path = r"D:/Dropbox/Music2Songs"
folder_paths = [os.path.join(parent_folder_path, d) for d in os.listdir(parent_folder_path) if os.path.isdir(os.path.join(parent_folder_path, d))]

folder_paths = [
    # "D:/Dropbox/Music2Songs/SYSTEM_COMMODO_DUBS",
    "D:/Dropbox/Music2Songs/TIPPER_RESLANG_type",
    # "D:/Dropbox/Music2Songs/uk_breakbeat_120_130_140",
    # "D:/Dropbox/Music2Songs/unclassified",
    # "D:/Dropbox/Music2Songs/WHACKLACK_type_groovy_halftime",
    # "D:/Dropbox/Music2Songs/2000s_nostalgic",
    # "D:/Dropbox/Music2Songs/acappellas",
    # "D:/Dropbox/Music2Songs/acid_house_grage",
    # "D:/Dropbox/Music2Songs/afro_house",
    # "D:/Dropbox/Music2Songs/aggro_110",
    # "D:/Dropbox/Music2Songs/aggro_150_160",
    # "D:/Dropbox/Music2Songs/aggro_clinical_dnb",
    # "D:/Dropbox/Music2Songs/aggro_clinical_halftime",
    # "D:/Dropbox/Music2Songs/aggro_crunchdubs_headland_epoch",
    # "D:/Dropbox/Music2Songs/aggro_crunchy_dnb_4x4",
    # "D:/Dropbox/Music2Songs/aggro_crunchy_IVYLAB_halftime",
    # "D:/Dropbox/Music2Songs/aggro_doubletime_140",
    # "D:/Dropbox/Music2Songs/aggro_dubstep_trap",
    # "D:/Dropbox/Music2Songs/aggro_jungle_breakcore_stinkers",
    # "D:/Dropbox/Music2Songs/aggro_KURSA_neuro_halftime",
    # "D:/Dropbox/Music2Songs/aggro_rap_modern_bangers",
    # "D:/Dropbox/Music2Songs/aggro_SHADES_150-160",
    # "D:/Dropbox/Music2Songs/aggro_SUPERTASK_slowbois",
    # "D:/Dropbox/Music2Songs/aggro_ternion_dubstep",
    # "D:/Dropbox/Music2Songs/aggro_ukg_house_bangers",
    # "D:/Dropbox/Music2Songs/aggro_wonky_minimal_dubntrap",
    # "D:/Dropbox/Music2Songs/bass_house",
    # "D:/Dropbox/Music2Songs/boombap_instrumentals_etc",
    # "D:/Dropbox/Music2Songs/boombap_lofi_beets",
    # "D:/Dropbox/Music2Songs/boombap_rap_hiphop",
    # "D:/Dropbox/Music2Songs/cafe_music",
    # "D:/Dropbox/Music2Songs/DREDD_type",
    # "D:/Dropbox/Music2Songs/eerie_dark_osiris_type",
    # "D:/Dropbox/Music2Songs/eerie_DDD_dubstep",
    # "D:/Dropbox/Music2Songs/eerie_deconstructed",
    # "D:/Dropbox/Music2Songs/eerie_gooood_dubs",
    # "D:/Dropbox/Music2Songs/eerie_halftime",
    # "D:/Dropbox/Music2Songs/eerie_house",
    # "D:/Dropbox/Music2Songs/fast_house",
    # "D:/Dropbox/Music2Songs/french_or_disco_house",
    # "D:/Dropbox/Music2Songs/fucking_ridiculous_nonsens",
    # "D:/Dropbox/Music2Songs/funk_neosoul_modern",
    # "D:/Dropbox/Music2Songs/funk_or_soul_classics",
    # "D:/Dropbox/Music2Songs/funkbap_big_GRAMATIK_PL_GRIZ",
    # "D:/Dropbox/Music2Songs/GJONES_EPROM_brokentype",
    # "D:/Dropbox/Music2Songs/groovy_dnb_classic_n_clinical",
    # "D:/Dropbox/Music2Songs/groovy_dubstep_drill_jazzy",
    # "D:/Dropbox/Music2Songs/groovy_EMUNE_houston_typebeets",
    # "D:/Dropbox/Music2Songs/groovy_halftime",
    # "D:/Dropbox/Music2Songs/groovy_jungle_classic",
    # "D:/Dropbox/Music2Songs/groovy_misc",
    # "D:/Dropbox/Music2Songs/groovy_ukg_uk_house",
    # "D:/Dropbox/Music2Songs/hiphop_rap_non_english",
    # "D:/Dropbox/Music2Songs/jazz",
    # "D:/Dropbox/Music2Songs/jazz_house",
    # "D:/Dropbox/Music2Songs/JPEGMafia",
    # "D:/Dropbox/Music2Songs/lofi_or_vibey_or_funk_house",
    # "D:/Dropbox/Music2Songs/maximal_trap_beets",
    # "D:/Dropbox/Music2Songs/My Finished Songs 10-31",
    # "D:/Dropbox/Music2Songs/pop_classics",
    # "D:/Dropbox/Music2Songs/pop_modern",
    # "D:/Dropbox/Music2Songs/pretty_COMTRUISE_HOME_type",
    # "D:/Dropbox/Music2Songs/pretty_deconstructed",
    # "D:/Dropbox/Music2Songs/pretty_dnb_JUNGLE",
    # "D:/Dropbox/Music2Songs/pretty_dubstep_140ish",
    # "D:/Dropbox/Music2Songs/pretty_halftime",
    # "D:/Dropbox/Music2Songs/pretty_melodic_hype",
    # "D:/Dropbox/Music2Songs/pretty_misc",
    # "D:/Dropbox/Music2Songs/pretty_SUPERTASK_slowbois",
    # "D:/Dropbox/Music2Songs/pretty_ukg_house_ukbreakbeat",
    # "D:/Dropbox/Music2Songs/rap_hiphop_classics",
    # "D:/Dropbox/Music2Songs/rnb_sexii",
    # "D:/Dropbox/Music2Songs/rock_folk_classics",
    # "D:/Dropbox/Music2Songs/slow_dance"
]



# Here is the list of all the folders containing music
folder_paths_to_ignore = [
    # "D:/Dropbox/Music2Songs/SYSTEM_COMMODO_DUBS",
    # "D:/Dropbox/Music2Songs/TIPPER_RESLANG_type",
    # "D:/Dropbox/Music2Songs/uk_breakbeat_120_130_140",
    "D:/Dropbox/Music2Songs/unclassified",
    "D:/Dropbox/Music2Songs/WHACKLACK_type_groovy_halftime",
    "D:/Dropbox/Music2Songs/2000s_nostalgic",
    "D:/Dropbox/Music2Songs/acappellas",
    "D:/Dropbox/Music2Songs/acid_house_grage",
    "D:/Dropbox/Music2Songs/afro_house",
    "D:/Dropbox/Music2Songs/aggro_110",
    "D:/Dropbox/Music2Songs/aggro_150_160",
    # "D:/Dropbox/Music2Songs/aggro_clinical_dnb",
    "D:/Dropbox/Music2Songs/aggro_clinical_halftime",
    # "D:/Dropbox/Music2Songs/aggro_crunchdubs_headland_epoch",
    # "D:/Dropbox/Music2Songs/aggro_crunchy_dnb_4x4",
    # "D:/Dropbox/Music2Songs/aggro_crunchy_IVYLAB_halftime",
    # "D:/Dropbox/Music2Songs/aggro_doubletime_140",
    # "D:/Dropbox/Music2Songs/aggro_dubstep_trap",
    # "D:/Dropbox/Music2Songs/aggro_jungle_breakcore_stinkers",
    "D:/Dropbox/Music2Songs/aggro_KURSA_neuro_halftime",
    "D:/Dropbox/Music2Songs/aggro_rap_modern_bangers",
    "D:/Dropbox/Music2Songs/aggro_SHADES_150-160",
    "D:/Dropbox/Music2Songs/aggro_SUPERTASK_slowbois",
    "D:/Dropbox/Music2Songs/aggro_ternion_dubstep",
    # "D:/Dropbox/Music2Songs/aggro_ukg_house_bangers",
    "D:/Dropbox/Music2Songs/aggro_wonky_minimal_dubntrap",
    "D:/Dropbox/Music2Songs/bass_house",
    "D:/Dropbox/Music2Songs/boombap_instrumentals_etc",
    "D:/Dropbox/Music2Songs/boombap_lofi_beets",
    "D:/Dropbox/Music2Songs/boombap_rap_hiphop",
    "D:/Dropbox/Music2Songs/cafe_music",
    "D:/Dropbox/Music2Songs/DREDD_type",
    # "D:/Dropbox/Music2Songs/eerie_dark_osiris_type",
    "D:/Dropbox/Music2Songs/eerie_DDD_dubstep",
    # "D:/Dropbox/Music2Songs/eerie_deconstructed",
    # "D:/Dropbox/Music2Songs/eerie_gooood_dubs",
    "D:/Dropbox/Music2Songs/eerie_halftime",
    "D:/Dropbox/Music2Songs/eerie_house",
    "D:/Dropbox/Music2Songs/fast_house",
    "D:/Dropbox/Music2Songs/french_or_disco_house",
    "D:/Dropbox/Music2Songs/fucking_ridiculous_nonsens",
    "D:/Dropbox/Music2Songs/funk_neosoul_modern",
    "D:/Dropbox/Music2Songs/funk_or_soul_classics",
    "D:/Dropbox/Music2Songs/funkbap_big_GRAMATIK_PL_GRIZ",
    "D:/Dropbox/Music2Songs/GJONES_EPROM_brokentype",
    # "D:/Dropbox/Music2Songs/groovy_dnb_classic_n_clinical",
    # "D:/Dropbox/Music2Songs/groovy_dubstep_drill_jazzy",
    "D:/Dropbox/Music2Songs/groovy_EMUNE_houston_typebeets",
    "D:/Dropbox/Music2Songs/groovy_halftime",
    # "D:/Dropbox/Music2Songs/groovy_jungle_classic",
    "D:/Dropbox/Music2Songs/groovy_misc",
    # "D:/Dropbox/Music2Songs/groovy_ukg_uk_house",
    "D:/Dropbox/Music2Songs/hiphop_rap_non_english",
    "D:/Dropbox/Music2Songs/jazz",
    "D:/Dropbox/Music2Songs/jazz_house",
    "D:/Dropbox/Music2Songs/JPEGMafia",
    "D:/Dropbox/Music2Songs/lofi_or_vibey_or_funk_house",
    "D:/Dropbox/Music2Songs/maximal_trap_beets",
    "D:/Dropbox/Music2Songs/My Finished Songs 10-31",
    "D:/Dropbox/Music2Songs/pop_classics",
    "D:/Dropbox/Music2Songs/pop_modern",
    "D:/Dropbox/Music2Songs/pretty_COMTRUISE_HOME_type",
    # "D:/Dropbox/Music2Songs/pretty_deconstructed",
    # "D:/Dropbox/Music2Songs/pretty_dnb_JUNGLE",
    # "D:/Dropbox/Music2Songs/pretty_dubstep_140ish",
    # "D:/Dropbox/Music2Songs/pretty_halftime",
    "D:/Dropbox/Music2Songs/pretty_melodic_hype",
    "D:/Dropbox/Music2Songs/pretty_misc",
    "D:/Dropbox/Music2Songs/pretty_SUPERTASK_slowbois",
    # "D:/Dropbox/Music2Songs/pretty_ukg_house_ukbreakbeat",
    "D:/Dropbox/Music2Songs/rap_hiphop_classics",
    "D:/Dropbox/Music2Songs/rnb_sexii",
    "D:/Dropbox/Music2Songs/rock_folk_classics",
    "D:/Dropbox/Music2Songs/slow_dance"
    ]

# for each folder path in the list
for folder_path in folder_paths:
    if folder_path not in folder_paths_to_ignore:
        # Get the name of the folder
        folder_name = os.path.basename(folder_path)

        # Loop through all files in this folder
        for filename in os.listdir(folder_path):
            try:
                encountered_files = []
                if filename.endswith(".flac"):
                    audio = flac.FLAC(os.path.join(folder_path, filename))
                    title = audio.get('title', [''])[0]
                    if title in encountered_files:
                        print(f"Duplicate found: {filename} with title {title}")
                    else:
                        encountered_files.append(title)
                
                    if audio.get('comment', '') != folder_name:
                        audio['comment'] = folder_name
                        # print(audio.get('comment', ''))
                    
                    if audio.get('genre', '') != folder_name:
                        audio['genre'] = folder_name

                    audio.save()

            except Exception as e:
                print(f'error with {filename}: {str(e)}')
                continue