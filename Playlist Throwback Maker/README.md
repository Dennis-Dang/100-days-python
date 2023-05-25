# Throwback Maker
This is an application that creates a spotify playlist for users and populates it with the top 100 ranking Billboard 
songs performing in the user-specified date (in YYYY-MM-DD format).

## How it works:
1. Ask the user what `date` they want to generate the playlist. (YYYY-MM-DD format)
2. Web scrape top 100 songs from Billboard based on date obtained from Step 1.
   - Billboard is a website that maintains a chart of top 100 performing songs based on the specific day of the year.
3. Connect to the api endpoint with api credentials.
4. Perform a search for the songs and generate a list of the corresponding spotify `track uri` matching it.
   - In case the track/song is not found on spotify, they will be accounted and notified of this error in the final 
   output.
5. Create a new playlist to the user's account.
   - Playlist name will be determined by the date input from Step 1.
     - Naming convention: {date} Billboard 100
6. Populate user playlist with music tracks obtained.
7. Output the link to the playlist successfully generated to the console.

## Credits
- Spotify API - Main API used for connection.
- Spotipy Python Module - For simplifying the Spotify API interface with Python.
- Billboard - For aggregating top 100 songs.
- BeautifulSoup4 Python Module - Webscraping utilities

## Permissive use:
Billboard's web crawling policy ("robots.txt")
#### https://www.billboard.com/robots.txt
```commandline
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

User-agent: Swiftbot
 Crawl-delay: 5
Disallow: /?s=
Disallow: /*/?s=
Disallow: /search/
Disallow: /search?
Disallow: *?v02
Disallow: *?replytocom
User-agent: cXensebot
Crawl-delay: 5
Disallow: /*preview=true
Disallow: /*theme_preview=true
```