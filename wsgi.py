import os
from application.app import create_app

FLASK_CONFIG = "FLASK_CONFIG"
app = create_app(os.environ[FLASK_CONFIG])
