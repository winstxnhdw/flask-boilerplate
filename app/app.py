from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from server import init_server
from models import Model
from config import Config

app = init_server()
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    
    return render_template('index.html')

def main():

    port = app.config['PORT']
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
    main()
