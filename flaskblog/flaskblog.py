from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [

    {
        'author': 'Nachiket Bhujbal',
        'title': 'Blog Post 1',
        'content': 'First post content body',
        'date': 'March 31, 2020'
        },
    {
        'author': 'Nachiket Bhujbal',
        'title': 'HAPPY APRIL FOOLS',
        'content': 'April fools day! Hahah',
        'date': 'April 1, 2020'
        }
    ]


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
