from flask import Flask, render_template, request, redirect, url_for, flash

def create_website():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    
    blog_data = [
        {
            "author": "John Smith",
            "date": "15 Jan 2022",
            "title": "Some Awesome Post",
            "content": "Whatever you want to say. This is only a temporary blog post. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ex ante, sagittis a convallis at, cursus eget tortor. Nam sed leo ut neque hendrerit pellentesque. Vestibulum blandit est quis nibh imperdiet, eget finibus magna porttitor. Aenean viverra felis in metus pretium dapibus. Pellentesque et cursus velit. Mauris porta viverra lectus at interdum. Integer sit amet hendrerit diam, id mattis risus. Pellentesque placerat pretium nisi, lacinia feugiat lectus faucibus a. In nisl velit, convallis et lacus eget, lobortis accumsan urna. Pellentesque at arcu eu libero faucibus ultricies. Integer tristique odio vitae sapien mollis dictum. Proin mollis malesuada purus in bibendum.",
        },
        {
            "author": "Jane Doe",
            "date": "19 Feb 2022",
            "title": "Some Awesome Post",
            "content": "Whatever you want to say. This is only a temporary blog post. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ex ante, sagittis a convallis at, cursus eget tortor. Nam sed leo ut neque hendrerit pellentesque. Vestibulum blandit est quis nibh imperdiet, eget finibus magna porttitor. Aenean viverra felis in metus pretium dapibus. Pellentesque et cursus velit. Mauris porta viverra lectus at interdum. Integer sit amet hendrerit diam, id mattis risus. Pellentesque placerat pretium nisi, lacinia feugiat lectus faucibus a. In nisl velit, convallis et lacus eget, lobortis accumsan urna. Pellentesque at arcu eu libero faucibus ultricies. Integer tristique odio vitae sapien mollis dictum. Proin mollis malesuada purus in bibendum.",
        },
        {
            "author": "Ellen Jones",
            "date": "15 Jan 2022",
            "title": "Some Awesome Post",
            "content": "Whatever you want to say. This is only a temporary blog post. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ex ante, sagittis a convallis at, cursus eget tortor. Nam sed leo ut neque hendrerit pellentesque. Vestibulum blandit est quis nibh imperdiet, eget finibus magna porttitor. Aenean viverra felis in metus pretium dapibus. Pellentesque et cursus velit. Mauris porta viverra lectus at interdum. Integer sit amet hendrerit diam, id mattis risus. Pellentesque placerat pretium nisi, lacinia feugiat lectus faucibus a. In nisl velit, convallis et lacus eget, lobortis accumsan urna. Pellentesque at arcu eu libero faucibus ultricies. Integer tristique odio vitae sapien mollis dictum. Proin mollis malesuada purus in bibendum.",
        }
    ]

    @app.route("/home")
    def home():
        return render_template("index.html", title="Home", style="../static/home.css", blogs=blog_data)

    @app.route("/sign-up", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            email = request.form.get("email") # get data from <input name="email"/>
            name = request.form.get("name")
            password1 = request.form.get("password")
            password2 = request.form.get("password2")
            # check if passwords are the same
            if password1 != password2:
                flash("Passwords don't match!", category="error")
            elif len(password1) < 8:
                flash("Password is too short!", category="error")
            elif len(name) == 0 or "@" not in email:
                flash("Invalid name or email!", category="error")
            else:
                flash("Welcome " + name + " to Super Blogger", category="success")
                return redirect(url_for("home"))

        return render_template("sign_up.html", title="Sign Up", style="../static/sign_up.css")  # we dont need to tell this route about the blogs

    return app
