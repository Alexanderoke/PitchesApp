from flask import Flask, render_template,url_for
app = Flask(__name__)


pitches = [
    {
        'author': 'Alexander oke',
        'title': 'pitch 1',
        'content': 'First post content',
        'date_posted': 'Febuary 10, 2022',
    },
    {
        'author': 'Alex William',
        'title': 'pitch 2',
        'content': 'Second post content',
        'date_posted': 'Febuary 10, 2022',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)