from flask import *
import pytube as yt
app = Flask(__name__)


@app.route('/')
def start():

    url = request.form.get("url")
    return 'hello'

if __name__ == '__main__':
    app.run(host="192.168.0.213")
