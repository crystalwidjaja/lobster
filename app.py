# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template,redirect,url_for
#create a Flask instance

app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
    return render_template("home.html")
    
if __name__ == "__main__":
  app.run(port='80', host='127.0.0.1')
