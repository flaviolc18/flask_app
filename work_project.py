import flask

app = flask.Flask("work_project")

@app.route('/')
def index():
  return flask.render_template("index.html", name="test user")

app.run(debug=True, use_reloader=True)