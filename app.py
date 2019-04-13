from flask import Flask, request, redirect, url_for, render_template
from PIL import Image
import requests
import math
from io import BytesIO

app = Flask(__name__)


@app.route('/mozaika')
def make_mosaic():
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
    return redirect(url_for('make_mosaic'))


def modify_images(pic_url_list, x_res, y_res):
    """Function which gets images from urls and makes final mosaic image"""
    pic_list = []
    counter = 0
    size = len(pic_url_list)

    mosaic = Image.new("RGB", (x_res, y_res), "white")

    if size == 1:
        response = requests.get(pic_url_list[0])
        img = (Image.open(BytesIO(response.content)))
        img = img.resize((x_res, y_res))
        mosaic.paste(img)

    elif size == 2 or size == 3:
        for pic in pic_url_list:
            img_width = int(x_res / size)
            img_height = int(y_res)

            response = requests.get(pic)
            img = (Image.open(BytesIO(response.content)))
            img = img.resize((img_width, img_height))
            mosaic.paste(img, (counter * img_width, 0))
            counter += 1

    elif size == 4 or size == 6 or size == 8:
        for pic in pic_url_list:
            img_width = int(x_res / (size / 2))
            img_height = int(y_res / 2)

            response = requests.get(pic)
            img = (Image.open(BytesIO(response.content)))
            img = img.resize((img_width, img_height))
            mosaic.paste(img, ((counter % int(size / 2)) * img_width, int(counter / int(size / 2)) * img_height))
            counter += 1

    elif size == 5 or size == 7:
        for pic in pic_url_list:
            if counter < int((size / 2)):
                img_width = int(x_res / int((size / 2)))
                img_height = int(y_res / 2)

                response = requests.get(pic)
                img = (Image.open(BytesIO(response.content)))
                img = img.resize((img_width, img_height))
                mosaic.paste(img, ((counter % int(size / 2)) * img_width, 0))
                counter += 1
            else:
                img_width = int(x_res / int(math.ceil(size / 2)))
                img_height = int(y_res / 2)

                response = requests.get(pic)
                img = (Image.open(BytesIO(response.content)))
                img = img.resize((img_width, img_height))
                mosaic.paste(img, ((counter-(int((size / 2)))) * img_width, img_height))
                counter += 1

    mosaic.show()


if __name__ == '__main__':
    app.run(debug=True)
