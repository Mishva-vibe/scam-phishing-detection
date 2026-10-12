```python
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    url = ""
    risk_level = ""
    risk_class = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        points = 0

        if "@" in url:
            points += 1

        if not url.lower().startswith("https://"):
            points += 1

        suspicious_words = ["login", "verify", "account", "bank", "password"]
        points += sum(1 for word in suspicious_words if word in url.lower())

        if len(url) > 75:
            points += 1

        if url.count(".") > 3:
            points += 1

        if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
            points += 1

        score = min(100, round((points / 10) * 100))

        if score < 30:
            risk_level, risk_class = "Low Risk", "safe"
        elif score < 60:
            risk_level, risk_class = "Suspicious", "warning"
        else:
            risk_level, risk_class = "High Risk", "danger"

    return render_template(
        "index.html",
        score=score,
        url=url,
        risk_level=risk_level,
        risk_class=risk_class
    )

if __name__ == "__main__":
    app.run(debug=True)
```
