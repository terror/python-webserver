import json
from flask import Flask, request

app   = Flask(__name__)
store = {}

@app.route('/')
def index():
  return 'Index', 200

@app.route('/set', methods = ['POST'])
def set():
  for key, value in request.args.items():
    store[key] = value
  return f'{json.dumps(store, indent = 2)}\n', 200

@app.route('/get', methods = ['GET'])
def get():
  key = request.args.get('key', default=None, type=str)
  if key and key in store:
    return f'{key} = {store[key]}\n'
  return 'Key not found.\n', 404

@app.route('/remove', methods = ['DELETE'])
def remove():
  key = request.args.get('key', default=None, type=str)
  if key and key in store:
    del store[key]
    return f'{json.dumps(store, indent = 2)}\n', 200
  return 'Key not found.\n', 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4000)
