from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/persona/<id>')
def persona(id):
    return render_template('persona.html', id=id)

if __name__ == '__main__':
    app.run(port=8080)
