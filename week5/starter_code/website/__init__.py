from flask import Flask, render_template

def create_website():
    app = Flask(__name__)
    
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

    return app
