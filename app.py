from flask import Flask, render_template, request

from lib.aws import get_workmail_aliases, get_workmail_domains
from lib.random_word import random_word as generate_random_word

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html.jinja2",
        aliases=get_workmail_aliases(),
        domains=get_workmail_domains(),
    )


@app.patch("/random_word")
def random_word():
    alias_length = request.form.get("alias-length", type=int)

    return render_template(
        "alias_input_field.html.jinja2", random_word=generate_random_word(alias_length)
    )


if __name__ == "__main__":
    app.run()
