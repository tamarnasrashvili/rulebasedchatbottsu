from app import app, Question
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from app import routes
if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=4761)
