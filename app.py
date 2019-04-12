from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/mozaika')
def mosaic():
    request_arguments = request.args.to_dict(flat=False)
    return request_arguments.__repr__()


@app.route('/')
def entry_page():
    return redirect(url_for('mosaic'))


if __name__ == '__main__':
    app.run(debug=True)
