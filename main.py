from flask import *
import pytube
app = Flask(__name__)
url = ""
userid = 0
id = 0
@app.route('/', methods=["GET", "POST"])
def start():
    global userid
    global url
    global id
    if request.method == "POST":
        url = request.form.get("url")
        id = id + 1
        userid = userid + 1
        yt = pytube.YouTube(url)
        videoname = str(userid)
        type = request.form.get('type')
        if type == 'mp3':
            map = (str(id) + ".mp3")
            yt.streams.filter(only_audio=True).first().download("downloads/" + videoname + "/", filename=map)
            returns = ("downloads/" + videoname + "/" + map)
            return send_file(
                returns,
                mimetype="audio/mpeg",
                as_attachment= True,
                download_name = 'download.mp3',
            )
        elif type == 'mp4':
           map1 = (str(id) + ".mp4")
           yt.streams.get_highest_resolution().download("downloads/" + videoname + "/", filename=map1)
           returns= ("downloads/" + videoname + "/" + map1)
           return send_file(returns, as_attachment=True)
        else:
            return("404.html")
    return render_template("start.html")
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def not_found(e):
    return render_template("500.html")
app.run()
