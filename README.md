# crate-folder-tool

### ohhhkayyyy so check it.

The way i organize my music crates is by computer folder in dropbox. I put all my acappellas in the folder 'acappellas', I put all my super high-energy aggressive bangers into the folder 'maximal_bangers'...etc etc. 

I do this so I can preserve my crates/playlists and quickly move from one dj software to another. It's also really nice because it means I can build crates and sort music no matter where I am or what computer I have at hand. 

However, the thing that's really annoying about this is <em>there's no way to sync all these playlists when changes happen in the folders</em>. So let's say I move a bunch of music out of the 'unclassified' folder into several other folders. I would then have to re-analyze the 'unclassified' folder to remove the items that the dj software can't find, and then go into each individual playlist and drag 'n drop the folder contents. Very annoying.

My script here solves the problem by scanning each of the folder paths you feed into the list at the top, then adding a TXXX frame with a commment containing the folder name. What this allows you to do is build intelligent playlists in rekordbox (smart crates in serato, Smart playlists in Engine DJ) which are based on those comment attributes in the id3 tag. Yes this is for mp3's. If anyone cares that much I can rewrite it to accommodate other formats.
