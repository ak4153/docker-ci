from flask import Flask
from redis import Redis
import os
app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis = Redis(host=redis_host, port=6379)
@app.route('/')
def hello_world():
    redis.incr('hits',amount=1)
    return '<html><body><h1>Hello, World!</h1></body></html>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)