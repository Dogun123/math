from flask import Flask,Blueprint
from flask.templating import render_template

app = Flask(__name__,static_url_path='/static')

app.register_blueprint('view.calc',url_prefix='calc')

@app.route('/')
def cover():
    return render_template('starter.html')

if __name__ == '__main__':
    app.run(host='localhost',port='5050',debug=True)