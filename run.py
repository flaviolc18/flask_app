from app import create_app
from settings import PROJECT_ROOT

app = create_app(PROJECT_ROOT + "/settings.py")

app.run(debug=True, use_reloader=True)

