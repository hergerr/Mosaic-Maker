from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/mozaika')
def mosaic():
    # default values of requst arguments
    x_resolution = 2048
    y_resolution = 2048
    random = False

    request_arguments = request.args.to_dict(flat=False)
    # check if optional argument (random) exists
    if 'losowo' in request_arguments and request_arguments['losowo'][0] == '1':
        random = True

    # check if option argument (resolution) exists
    if 'rozdzielczosc' in request_arguments:
        # splitting x and y resolution values by 'x' and mapping it on int
        x_resolution, y_resolution = map(int, request_arguments['rozdzielczosc'][0].split('x'))

    if 'zdjecia' in request_arguments:
        pic_list = request_arguments['zdjecia'][0].split(',')

    print(pic_list)
    return render_template('mosaic.html', pic_list=pic_list)


@app.route('/')
def entry_page():
    return redirect(url_for('mosaic'))


if __name__ == '__main__':
    app.run(debug=True)
