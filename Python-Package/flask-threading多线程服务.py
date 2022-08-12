import json,time
import flask
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()
@app.route('/')
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    return json.dumps({
        'read_file':result_file.result(),
        'read_db':result_db.result(),
        'read_api':result_api.result()
    })
def read_file():
    time.sleep(1)
    return 'file result'
def read_db():
    time.sleep(2)
    return 'db result'
def read_api():
    time.sleep(3)
    return 'api result'
if __name__ == "__main__":
    app.run()