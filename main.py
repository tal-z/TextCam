from flask import Flask, render_template
from grayscale import *

app = Flask(__name__)



@app.route("/")
def hello_world():
    filepath = r"C:\Users\PC\Pictures\peppers.jpg"
    img = Image.open(filepath)
    text = img2text(img)
    html = format_html(text, img.size)
    return render_template('index.html', html=html)

if __name__ == '__main__':
    app.run(debug=True)