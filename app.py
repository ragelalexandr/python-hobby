from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Python Hobby</h1> <p>https://python-hobby.vercel.app/</p> <p><a href="mailto:ragel.alexandr@gmail.com">ragel.alexandr@gmail.com</a> </p> <p><a href="tel:+375298608038">+375(29)860-80-38</a>   </p>'
if __name__ == '__main__':
    app.run(debug=True)