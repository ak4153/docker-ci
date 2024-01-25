from flask import Flask
from redis import Redis
app = Flask(__name__)

redis = Redis(host='redis', port=6379)
@app.route('/')
def hello_world():
    redis.incr('hits',amount=1)
    return f'<html><head><title>Python Web Page</title></head><body><h1>hits:{redis.get("hits")}</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)