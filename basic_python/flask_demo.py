from flask import Flask
import datetime 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/KIET')
def kiet():
    date = str(datetime.datetime.now())
    return date

if __name__ == '__main__':
    app.run(debug=True)
