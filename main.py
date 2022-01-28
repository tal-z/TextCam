
import base64

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from image2text import *


app = Flask(__name__)

default_img = r"C:\Users\PC\Pictures\bat_signal.png"

FPS = 32

shot_idx = 0
html_shots = []

@app.route("/webcam2text")
def webcam2text():
    filepath = request.args.get('imageBase64') or default_img
    content = filepath.split(';')[1]
    image_encoded = content.split(',')[1]
    shot = base64.decodebytes(image_encoded.encode('utf-8'))
    img = Image.open(BytesIO(shot))
    img.thumbnail((200,200))
    text = img2text(img)
    html = format_html(text, img.size)
    html_shots.append(html)
    return Response(200)


@app.route("/webcam_feed/")
def webcam_feed():
    global html_shots
    if not html_shots:
        return render_template('webcam_feed.html', html="No Live Feed", FPS=FPS)
    global shot_idx
    html_shots = [html_shots.pop()]
    html = html_shots
    return render_template('webcam_feed.html', html=html, FPS=FPS)



@app.route('/view_webcam')
def view_webcam():
    return render_template('view_webcam.html', FPS=FPS)


@app.route("/webcam")
def webcam():
    return render_template('webcam.html', FPS=FPS)


@app.route("/image2text")
def image2text():
    filepath = request.args.get('filepath') or default_img
    print(filepath)
    img = get_pillow_img(filepath)
    img.thumbnail((200,200))
    text = img2text(img)
    html = format_html(text, img.size)
    return render_template('image2text.html', html=html)




if __name__ == '__main__':
    app.run(debug=True, threaded=True)