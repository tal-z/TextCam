
import base64

from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from image2text import *

app = Flask(__name__)

default_img = r"C:\Users\PC\Pictures\bat_signal.png"

FPS = 32
html_shots = []

@app.route("/webcam2text", methods=['POST'])
def webcam2text():
    print('hit route')
    filepath = request.args.get('imageBase64') or default_img
    content = filepath.split(';')[1]
    image_encoded = content.split(',')[1]
    shot = base64.decodebytes(image_encoded.encode('utf-8'))
    img = Image.open(BytesIO(shot))
    img.thumbnail((200,200))
    text = img2text(img)
    html = format_html(text, img.size)
    html_shots.append(html)
    print("html_shots:", len(html_shots)-1)
    return jsonify(success=True)


@app.route("/webcam2text_burst", methods=['POST'])
def webcam2text_burst():
    global html_shots
    images = request.form.getlist("image_data")
    for image in images[0].split(','):
        try:
            image_encoded = image
            shot = base64.decodebytes(image_encoded.encode('utf-8'))
            img = Image.open(BytesIO(shot))
            img.thumbnail((200, 200))
            text = img2text(img)
            html = format_html(text, img.size)
            html_shots.append(html)
            #print("html_shots:", len(html_shots)-1)
        except:
            pass
            #print("EXCEPTION ON:", image)
    return jsonify(success=True)


@app.route("/webcam_feed/")
def webcam_feed():
    if not html_shots:
        return render_template('webcam_feed.html', html="No Live Feed", FPS=FPS)
    try:
        html = html_shots.leftpop()
    except:
        html = html_shots[-1]
    return render_template('webcam_feed.html', html=html, FPS=FPS)


@app.route("/webcam_feed_json")
def webcam_feed_json():
    try:
        html = html_shots.leftpop()
    except:
        html = html_shots[-1]
    return jsonify({'html': html})


last = 0
@app.route("/webcam_feed_json_burst")
def webcam_feed_json_burst():
    global html_shots
    try:
        html_shots = html_shots[-FPS:]
        print("tried successfully", len(html_shots))
    except:
        print('failed exceptionally')
    return jsonify({'html_burst': html_shots})



@app.route('/viewer')
def viewer():
    return render_template('viewer.html', FPS=FPS)


@app.route("/recorder")
def recorder():
    return render_template('recorder.html', FPS=FPS)




@app.route("/image2text")
def image2text():
    filepath = request.args.get('filepath') or default_img
    print(filepath)
    img = get_pillow_img(filepath)
    img.thumbnail((100,100))
    text = img2text(img)
    html = format_html(text, img.size)
    return render_template('image2text.html', html=html)




if __name__ == '__main__':
    app.run(debug=True, threaded=True)
