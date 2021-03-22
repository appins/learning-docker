import redis
from flask import Flask
import sys
app = Flask(__name__)

r = None

@app.route('/cat')
def cat():
    return r.get('cat').decode('utf-8')

@app.route('/dog')
def dog():
    return r.get('dog').decode('utf-8')

@app.route('/votedog')
def votedog():
    val = int(r.get('dog').decode('utf-8')) + 1
    r.set('dog', val)
    return "Success"

@app.route('/votecat')
def votecat():
    val = int(r.get('cat').decode('utf-8')) + 1
    r.set('cat', val)
    return "Success"

if __name__ == '__main__':
    r = redis.Redis(host='redis', port=6379, db=0)
    if r.get('cat') is None or r.get('dog') is None:
        r.set('cat', 0)
        r.set('dog', 0)
    app.run(host='0.0.0.0')

