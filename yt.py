import subprocess
import os

playlist = 'https://youtube.com/playlist?list=PLBQN695cn7RIVHRVLIYzmuDoT517BiSlZ'
ydl_opts = "D:/spotify_dl/songs/"
for file_name in os.listdir(ydl_opts):
    var = ydl_opts + file_name
    os.remove(var)
str1 = 'youtube-dl -f bestaudio[ext=m4a] --embed-thumbnail -o ' + \
    ydl_opts + '\%(title)s.%(ext)s ' + playlist

with open('D:\spotify_dl\output.txt', 'w') as out:
    with open('D:\spotify_dl\error.txt', 'w') as err:
        process = subprocess.run(
            ['cmd', '/c', str1], check=True, capture_output=True, text=True)
        out.write(process.stdout)
        err.write(process.stderr)
