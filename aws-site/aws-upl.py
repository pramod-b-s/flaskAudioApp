from flask import Flask, render_template, request, make_response, stream_with_context, send_from_directory, flash, Response, send_file, after_this_request
import youtube_dl
import os

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'outtmpl': '/home/pramod/Desktop/flaskSite/MyYoutubeSong.mp3',
}

app = Flask(__name__)

@app.route('/')
def upload_file():
	return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def uploaded_file_msg():
	link = request.form['text1']
	print(link+"--link--")

	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info_dict = ydl.extract_info(link, download=True)
		# print("duration  "+format['end_time'])
		video_url = info_dict.get("url", None)
		video_id = info_dict.get("id", None)
		video_id.replace(" ", "_")
		print(video_id)
		video_title = info_dict.get('title', None)
		video_title.replace(" ", "_")
		print(video_title)
		filename=video_title+video_id+".mp3"
		# filename="form.mp3"

	path=os.path.normpath('/home/flaskSite/MyYoutubeSong.mp3')
	
	@after_this_request
	def remove_file(response):
		print("----------removing file generated-------")
		os.remove(path)
		return response

	return send_file(path, as_attachment=True)


if __name__ == '__main__':
	app.run(debug = True)