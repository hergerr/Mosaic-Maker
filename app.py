from flask import Flask, request, redirect, url_for, render_template
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)


@app.route('/mozaika')
def mosaic():
    """This function deals with given url and returns template with mosaic"""

    # list with url for pictures
    pic_url_list = []

    # default resolution
    x_resolution = 2048
    y_resolution = 2048

    request_arguments = request.args.to_dict(flat=False)
    # check if option argument (resolution) exists
    if 'rozdzielczosc' in request_arguments:
        # splitting x and y resolution values by 'x' and mapping it on int
        x_resolution, y_resolution = map(int, request_arguments['rozdzielczosc'][0].split('x'))

    if 'zdjecia' in request_arguments:
        pic_url_list = request_arguments['zdjecia'][0].split(',')

    # check if optional argument (random) exists
    if 'losowo' in request_arguments and request_arguments['losowo'][0] == '1':
        map(set, pic_url_list)

    modify_images(pic_url_list, x_resolution, y_resolution)

    return render_template('mosaic.html')


@app.route('/')
def entry_page():
    return redirect(url_for('mosaic'))


def modify_images(pic_url_list, x_res, y_res):
    """Function which gets images from urls and makes final mosaic image"""
    pic_list = []

    for pic in pic_url_list:
        size = len(pic_url_list)

        response = requests.get(pic)
        img = (Image.open(BytesIO(response.content)))
        img = img.resize((int(x_res / size), int(y_res / size)))
        pic_list.append(img)

    for pic in pic_list:
        pic.show()


if __name__ == '__main__':
    app.run(debug=True)
