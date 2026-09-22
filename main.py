from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        score = 0

        if "@" in url:
            score += 1

        if not url.startswith("https://"):
            score += 1

        if any(word in url.lower() for word in ["login", "verify", "account", "bank", "password"]):
            score += 1

        if len(url) > 75:
            score += 1

        if url.count(".") > 3:
            score += 1

        if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
            score += 1

        score = (score / 6) * 100

    return render_template("index.html", score=score, url=url)

if __name__ == "__main__":
    app.run(debug=True)
