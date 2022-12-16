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
        map = (str(id) + ".mp4")
        yt = pytube.YouTube(url)
        videoname = str(userid)
        yt.streams.get_highest_resolution().download("downloads/" + videoname + "/", filename=map)
        returns = ("downloads/" + videoname + "/" + map)
        return send_file(returns, as_attachment=True)
    return render_template("start.html")
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def not_found(e):
    return render_template("500.html")
app.run()
