from flask import Flask, render_template

def create_website():
    app = Flask(__name__)
    
    @app.route("/home")
    def home():
        return render_template("index.html")

    return app
