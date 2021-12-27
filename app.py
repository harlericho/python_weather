from os import device_encoding
from flask import Flask, render_template, request
from weather import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    city = request.form.get('city')
    # print(city)
    return render_template('index.html', town = weather(city))


if __name__ == '__main__':
    app.run(port=5000, debug=True)