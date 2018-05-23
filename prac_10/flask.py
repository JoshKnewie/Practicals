from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)


@app.route('/f/')
@app.route('/f/<temp>')
def f(temp):
    celsius = 5 / 9 * (float(temp) - 32)
    return 'Fahrenheit {} is {} in celsius'.format(temp, celsius)


if __name__ == '__main__':
    app.run()
