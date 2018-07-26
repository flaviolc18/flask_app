from flask import Flask

app = Flask("work_project")

@app.route('/')
def index():
  return "it works!", 200

app.run(debug=True, use_reloader=True)