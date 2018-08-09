import sys
from app import create_app

mode = sys.argv[1] if len(sys.argv) > 1 else "development"
app = create_app(mode=mode)

app.run(debug=True, use_reloader=True)

