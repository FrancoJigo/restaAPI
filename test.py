from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    r = requests.get('http://127.0.0.1:5000/secrets')
    json_object = r.json()
    
    return render_template('home2.html', json_object = json_object)



if __name__ == '__main__':
    app.run()