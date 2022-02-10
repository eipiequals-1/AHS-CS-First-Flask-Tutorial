from flask import Flask

website = Flask(__name__)

@website.route("/home")
def home():
    return "Hello World"

if __name__ == "__main__":
    website.run(debug=True)
