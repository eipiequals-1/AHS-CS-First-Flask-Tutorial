from flask import Flask, render_template

website = Flask(__name__)

@website.route("/home")
def home():
    names_of_people = ["John", "Jane", "Steve", "Bob"]
    # the data in names_of_people will be copied into a key "names"
    # "names" can be used as a variable in the html file
    return render_template("base.html", names=names_of_people)

if __name__ == "__main__":
    website.run(debug=True)
