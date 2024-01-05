import json
from flask import Flask, render_template, request
from traffic import Signal, Light

version = "Traffic Light V2.1 - 01/2024"

signals = [
    Signal(21, "red", "#ff0000"),
    Signal(12, "orange", "#ffa500"),
    Signal(16, "green", "#008000")
]

app = Flask(__name__)


@app.route('/')
def myindex():
    return version


@app.route('/status')
def status() -> str:
    result = []
    for item in signals:
        result.append(item.status())
    return json.dumps(result)


@app.route('/control')
def control():
    # here we want to get the value of user (i.e. ?signal=green)
    signal = request.args.get('signal', '')

    for item in signals:
        item.set_light(Light.ON if item.name == signal else Light.OFF)
    stat = json.loads(status())
    return render_template('control.html',
                           name=signal,
                           status=stat,
                           version=version)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
