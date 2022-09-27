from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home/index.html')

# ------------------------- Docs ----------------------------------------


@app.route('/docs')
def docs():
    return render_template('home/docs.html')

# ------------------------- Docs ----------------------------------------

# ------------------------- Orders ----------------------------------------


@app.route('/orders')
def orders():
    return render_template('home/orders.html')

# ------------------------- Orders ----------------------------------------


# ------------------------- Pages ---------------------------------------

@app.route('/notifications')
def notifications():
    return render_template('home/notifications.html')


@app.route('/account')
def account():
    return render_template('home/account.html')


@app.route('/settings')
def settings():
    return render_template('home/settings.html')

# ------------------------- Pages ---------------------------------------

# ------------------------- External ------------------------------------


@app.route('/login')
def login():
    return render_template('home/login.html')


@app.route('/signup')
def signup():
    return render_template('home/signup.html')


@app.route('/reset-password')
def reset_password():
    return render_template('home/reset-password.html')


@app.route('/404')
def four_not_four():
    return render_template('home/404.html')

# ------------------------- External ------------------------------------

# ------------------------- Charts --------------------------------------


@app.route('/charts')
def charts():
    return render_template('home/charts.html')

# ------------------------- Charts --------------------------------------


# ------------------------- Help ----------------------------------------


@app.route('/help')
def app_help():
    return render_template('home/help.html')

# ------------------------- Help ----------------------------------------


if __name__ == '__main__':
    app.run(port=8000)
