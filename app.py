from flask import Flask, render_template,redirect,url_for
import data

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", title = data.setup())
    
if __name__ == "__main__":
    app.run(debug = True, port=9090)
