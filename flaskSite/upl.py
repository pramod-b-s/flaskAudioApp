from flask import Flask, render_template, request, make_response, stream_with_context, send_from_directory, flash, Response, send_file, after_this_request
# from werkzeug import secure_filename
# from pygame import mixer
import youtube_dl
import os
# from shutil import copyfile
# from pydub import AudioSegment

# from functools import partial
# from subprocess import Popen, PIPE

# mp3file = 'shapeOfYou.mp3'

ctr=0

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
	# t1=request.form['beg_time']
	# t2=request.form['end_time']
	# print("start "+t1+" end "+t2)
	# if(t1>t2):
	# 	print("invalid times!!!")
	# 	err_response=make_response("Starting time must not be greater than ending time !!",404)
	# 	return(err_response)

	print(link+"--link--")
	
	# startMin = 0
	# startSec = 0
	# endMin = 2
	# endSec = 0

	# startTime = startMin*60*1000+startSec*1000
	# endTime = endMin*60*1000+endSec*1000
	
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

	# song=AudioSegment.from_mp3('/home/pramod/Desktop/flaskSite/MyYoutubeSong.mp3')
	# extract = song[startTime:endTime]

	path=os.path.normpath('/home/pramod/Desktop/flaskSite/MyYoutubeSong.mp3')
	
	@after_this_request
	def remove_file(response):
		print("----------removing file generated-------")
		os.remove(path)
		return response

	return send_file(path, as_attachment=True)



# @app.route('/download')  
# def download_file():
# 	return send_file('/home/pramod/Desktop/flaskSite/MyAwesomeMix.mp3', as_attachment=True)
# 	return response

# @app.route('/downloader', methods = ['GET', 'POST'])
# def download_file_msg():
# 	if request.method == 'POST':
# 		return send_from_directory(directory="/home/pramod/flaskSite/", filename='shapeOfYou.mp3', as_attachment=True)


# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file_msg():
# 	if request.method == 'POST':
# 		f = request.files['file']
# 		f.save(secure_filename(f.filename))
# 		return render_template('download.html')

if __name__ == '__main__':
	app.run(debug = True)


## CRAP CRAP CRAP CRAP CRAP  

	# # process = Popen(['cat', mp3file], stdout=PIPE, bufsize=-1)
	# # read_chunk = partial(os.read, process.stdout.fileno(), 1024)
	# # return Response(iter(read_chunk, b''), mimetype='audio/mp3')


	# # csv = 'foo,bar,baz\nhai,bai,crai\n'  
	# response=stream_with_context("shapeOfYou.mp3")
	# # response = make_response("Ed Sheeran Shape Of You.mp3")
	# Content-Type: audio/mpeg
	# cd = 'attachment; filename=shapeOfYou'
	# response.headers['Content-Disposition'] = cd 
	# response.mimetype='audio/mpeg'

	# return response

	# mp3file = open('/home/pramod/Desktop/flaskSite/shapeOfYou.mp3', 'r')
	# response = Response(stream_with_context(mp3file), mimetype='audio/mpeg',
	# 	headers={"Content-disposition":"attachment; filename=download.mp3","Content-Type": "audio/mpeg"})
	#response['Content-Disposition'] = "attachment; filename=test.mp3"
	# mp3file = '/home/pramod/Desktop/flaskSite/shapeOfYou.mp3'
	# return Response(stream_with_context(mp3file), mimetype="audio/mpeg3",
	# 	headers={"Content-disposition":"attachment; filename=download.mp3","Content-Type": "audio/mpeg3"})