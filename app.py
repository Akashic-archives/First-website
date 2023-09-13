from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/horaire")
def horaire():
    return render_template("horaire.html")

@app.route("/tos")
def tos():
    return render_template("tos.html")

#@app.route("/forensics")
#def home():
#    return render_template("horaire.html")

#@app.route("/cv")
#def home():
#    return render_template("cv.html")

#@app.route("/index")
#def home():
#    return render_template("index.html")

#@app.route("/moi")
#def home():
#    return render_template("moi.html")

#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}"

#@app.route("/admin")
#def admin():
#    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80) #port=xxxx

