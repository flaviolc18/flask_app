from flask import (Flask, render_template, request)

app = Flask("work_project")

@app.route('/')
def index():
  return render_template("main.html", name="test user")

#try only with the post
@app.route('/handlead', methods=["GET", "POST"])
def handlead():
  if request.method == "POST":
    comp = request.form['comp']
    serv = request.form['serv']
    if comp and serv:
      return render_template("foundads.html", comp=comp, serv=serv)
    else:
      return render_template("main.html", error_msg="Fill all the the form")


app.run(debug=True, use_reloader=True)