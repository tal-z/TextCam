from PIL import Image


def get_pillow_img(name):
    img = Image.open(name)
    return img



def img2text(img):
    ascii_scale = {
        0: ' ',
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
    }
    img = img.convert('L')
    greyscale_data = list(img.getdata())
    return [ascii_scale[val // (img.height//10)] for val in greyscale_data]


def format_html(data, size):
    w = size[0]
    h = size[1]
    string = ''
    start, end = 0, w
    for row in range(h):
        string = string + "<br>"
        string += ''.join([str(item)+" " for item in data[start:end]])
        start += w
        end += w
    return string


if __name__ == '__main__':
    filepath = r"C:\Users\PC\Pictures\peppers.jpg"
    img = Image.open(filepath)
    text = img2text(img)
    html = format_html(text, img.size)
    print(html)
