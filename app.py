from os import environ

from flask import Flask, render_template, request, redirect, url_for, flash

from lib.aws import (
    get_workmail_aliases,
    get_workmail_domains,
    delete_workmail_alias,
    create_workmail_alias,
)
from lib.random_word import random_word as generate_random_word

app = Flask(__name__)
app.secret_key = environ.get("FLASK_SECRET_KEY")


@app.route("/")
def index():
    return render_template(
        "index.html.jinja2",
        aliases=get_workmail_aliases(),
        domains=get_workmail_domains(),
    )


@app.patch("/random_word")
def random_word():
    alias_length = request.form.get("alias-length", 16, type=int)

    return render_template(
        "alias_input_field.html.jinja2", random_word=generate_random_word(alias_length)
    )


@app.post("/alias/delete")
def delete_alias():
    alias = request.form.get("alias")
    try:
        delete_workmail_alias(alias)
        flash(f"Alias {alias} deleted", "success")
    except Exception as e:
        flash(f"Alias {alias} could not be deleted: {e}", "danger")

    return redirect(url_for("index"))


@app.post("/alias/create")
def create_alias():
    mailbox = request.form.get("mailbox")
    domain = request.form.get("domain")
    alias = f"{mailbox}@{domain}"
    try:
        create_workmail_alias(alias)
        flash(f"Alias {alias} created", "success")
    except Exception as e:
        flash(f"Alias {alias} could not be created: {e}", "danger")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
