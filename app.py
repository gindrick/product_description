import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["animal"]
        params = request.form["params"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name, params),
            temperature=0.6,            
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, params):
    return """Napiš mi prosím popis produktu na eshop aspoň na 300 slov pro produkt s názvem: {} a s parametry: {}""".format(
        name.capitalize(), params
    )

