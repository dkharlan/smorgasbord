from flask import Flask

app = Flask(__name__)


@app.route('/status')
def status() -> str:
    return 'OK'
