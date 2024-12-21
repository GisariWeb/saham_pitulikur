import os

from flask import Flask, send_file
from api import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/")
def index():
    return send_file('src/index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
