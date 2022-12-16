from flask import *
import pytube
app = Flask(__name__)
url = ""
#yt = pytube.YouTube(video_url)
#yt.streams.get_highest_resolution().download(path1)
@app.route('/', methods=["GET", "POST"])
def start():
    global url
    if (request.method == "POST"):
        url = request.form.get("url")
        video_url = url
    return render_template("load.html")


if __name__ == '__main__':
    app.run(host="192.168.0.213")
