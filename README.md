# crate-folder-tool

### ohhhkayyyy so check it.

The way i organize my music crates is by directory in dropbox. 

I do this so I can preserve my crates/playlists and quickly move from serato to rekordbox to engine prime as needed. It's also really nice because it means I can build crates and sort music no matter where I am or what computer I have at hand, as long as i can login to Dropbox to access my files there. 

However, the thing that's really annoying about this is <em>there's no way to sync all these playlists when changes happen in the folders</em>. So let's say I move a bunch of music out of the 'unclassified' folder into several other folders. I would then have to re-analyze the ENTIRE 'unclassified' folder to remove the items that the dj software can't find, and then go into each individual playlist and drag 'n drop the folder contents. Very annoying and time-consuming. Unfortunately nobody has built in a live folder sync that i can find, and I'm not tryna pay for rekordbox's dropbox integration. The Engine Prime integration didn't sync like i need it to either.

My script here solves the problem by scanning each of the folder paths you feed into the list at the top, then adding a TXXX frame with a commment containing the folder name. What this allows you to do is build intelligent playlists in rekordbox (smart crates in serato, Smart playlists in Engine DJ) which are based on those comment attributes in the id3 tag. Currently only works for mp3 and flac--wav is notoriously bad for metadata so i don't wanna go down that road. If anyone cares I can add a script to accommodate other formats.
