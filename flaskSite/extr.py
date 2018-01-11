from pydub import AudioSegment

song=AudioSegment.from_mp3('/home/pramod/Desktop/flaskSite/MyYoutubeSong.mp3')
extract = song[100:1000]