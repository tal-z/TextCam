
from io import BytesIO

import requests
from PIL import Image


def get_pillow_img(filepath):
    if not filepath[:4] == 'http':
        img = Image.open(filepath)
    else:
        response = requests.get(filepath, timeout=3)
        img = Image.open(BytesIO(response.content))
    return img


def img2text(img):
    ascii_scale = {
        0: '.',
        1: '^',
        2: '~',
        2: '"',
        3: '=',
        4: '+',
        5: '*',
        6: '&',
        7: '#',
        8: '%',
        9: '@',
        10: '♥'
    }
    img = img.convert('L')
    greyscale_data = list(img.getdata())
    return [ascii_scale[10-max(int(val // 25), 0)] for val in greyscale_data]


def format_html(data, size):
    w, h = size
    string = ''
    start, end = 0, w
    while end <= len(data):
        string += ''.join(data[start:end]) + '<br>'
        start = end
        end += w
    return string


if __name__ == '__main__':
    filepath = r"C:\Users\PC\Pictures\peppers.jpg"
    img = Image.open(filepath)
    text = img2text(img)
    html = format_html(text, img.size)
    print(html)
