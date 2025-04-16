from flask import Flask, render_template, request

app = Flask(__name__)

votes = {"Cats": 0, "Dogs": 0}

@app.route("/", methods=["GET", "POST"])
def index():
    global votes
    if request.method == "POST":
        if request.form.get("action") == "clear":
            votes = {"Cats": 0, "Dogs": 0}
        else:
            vote = request.form.get("animal")
            if vote in votes:
                votes[vote] += 1
    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

