from flask import Flask, render_template, abort
from flaski.models import WikiContent

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello():
    contents = WikiContent.query.all()
    return render_template("index.html", contents=contents)


@app.route("/<title>", methods=["GET"])
def show_content(title):
    content = WikiContent.query.filter_by(title=title).first()
    if content is None:
        abort(404)
    return render_template("show_content.html", content=content)

if __name__ == "__main__":
    app.run()
