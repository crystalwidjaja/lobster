# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template,redirect,url_for
#create a Flask instance

app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
@app.route('/landing_page')
def landing_page():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("landing_page.html")

@app.route('/home')
def home_route():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/all_galleries')
def all_galleries():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("all_galleries.html")

@app.route('/botany')
def botany():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("botany.html")

@app.route('/history')
def history():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("history.html")

@app.route('/japanese_culture')
def japanese_culture():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("japanese_culture.html")

@app.route('/music')
def music():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("music.html")

@app.route('/photography')
def photography():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("photography.html")

@app.route('/planetarium')
def planetarium():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("planetarium.html")

@app.route('/gift_shop')
def gift_shop():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("gift_shop.html")

@app.route('/about_us')
def about_us():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("about_us.html")

if __name__ == "__main__":
  app.run(port='80', host='127.0.0.1')
