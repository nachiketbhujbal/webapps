from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc643a510f94191f5e01e52938fbb866'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful!', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
