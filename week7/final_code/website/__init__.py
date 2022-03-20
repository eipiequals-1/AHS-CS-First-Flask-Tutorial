from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash

current_user = None
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
# store user names, emails, passwords in here
all_users = {}

def create_website():
    global current_user, blog_data, all_users
    app = Flask(__name__)
    app.secret_key = "super secret key"

    @app.route("/home")
    def home():
        return render_template("index.html", title="Home", style="../static/home.css", blogs=blog_data)

    @app.route("/sign-up", methods=["GET", "POST"])
    def signup():
        global current_user
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
                current_user = name
                # add user to all_users
                all_users[name] = {
                    "email": email,
                    "password": password1
                }
                print(all_users)
                flash("Welcome " + name + " to Super Blogger", category="success")
                return redirect(url_for("home"))

        return render_template("sign_up.html", title="Sign Up", style="../static/sign_up.css")  # we dont need to tell this route about the blogs

    @app.route("/new-post", methods=["GET", "POST"])
    def new_post():
        if current_user != None:  # if user is logged in then he/she has access to this route
            if request.method == "POST":
                post_title = request.form.get("post-title")
                post_content = request.form.get("post-content")
                # you can check if the title and content is valid if you want
                # but I'm not
                current_date = date.today()
                # format date if you want
                blog_data.append({
                    "author": current_user,
                    "date": str(current_date),
                    "title": post_title,
                    "content": post_content
                })
                return redirect(url_for("home"))

            # if GET HTTP request -> new_post.html
            return render_template("new_post.html", title="Create Post", style="../static/new_post.css")
        else:
            flash("Not Logged In!", category="error")
            return redirect(url_for("home"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        global current_user
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            for name, user_data in all_users.items():
                if user_data["email"] == email and user_data["password"] == password:
                    current_user = name
                    flash("Welcome back " + name + "!")
                    return redirect(url_for("home"))
            # if we made it here, logging in must have failed
            flash("Invalid email or password! Please Try Again!")

        return render_template("login.html", title="Login", style="../static/login.css")

    @app.route("/logout", methods=["GET"])
    def logout():
        global current_user
        current_user = None
        flash("You've been logged out!", category="success")
        return redirect(url_for("home"))

    return app
