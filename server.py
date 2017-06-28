#!flask/bin/python
from __future__ import print_function
import os
import dotenv # https://github.com/mattseymour/python-env
from flask import Flask, jsonify, request, make_response, abort
import json
import requests
import sys
import traceback
import logging

import site

def get_main_path():
    test_path = sys.path[0] # sys.path[0] is current path in 'examples' subdirectory
    split_on_char = "/"
    return split_on_char.join(test_path.split(split_on_char)[:-1])
main_path = get_main_path()
site.addsitedir(main_path+'/lib')
print ("Imported subfolder: %s" % (main_path+'/lib') )

import lib
from lib.main import main

# Flask class instance with RESTful web service 
# endpoints using single module
app = Flask(__name__)

# Load .env credentials
APP_ROOT = os.path.join(os.path.dirname(__file__), '')
dotenv_path = os.path.join(APP_ROOT, '.env')
dotenv.load(dotenv_path)

# GET Webhook
@app.route('/', methods=['GET'])
def handle_get():
    """
    Handles GET
    """
    print("Called handle_get in server.py with request: %r" % (json.dumps(request.json, indent=4, sort_keys=True)))
    sys.stdout.flush() # Capture in logs
    return "ok"

@app.route('/api/v1.0/query', methods=['GET'])
def get_query():
    """
    Main Examples:
        curl -i "http://localhost:5000/api/v1.0/query?query=None&my_param=abc"
        curl -i "http://localhost:5000/api/v1.0/query?query=test&my_param=def"
    """
    query_params = request.args.to_dict()
    if len(query_params) == 0:
        abort(400)
    print("Query Params: ", query_params, file=sys.stderr)

    def process(query_params):
        return main(query_params)
    answer = process(query_params)

    response = jsonify({'success': answer})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200, {'ContentType':'application/json'}

# POST Webhook
@app.route('/', methods=['POST'])
def handle_post():
    """
    Handle POST
    """
    print('Called handle_post in server.py with request: %r' % (json.dumps(request.json, indent=4, sort_keys=True)))
    return "ok"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':

    print("Called main in server.py and running Flask server")

    # Run Flask server
    app.run(host='127.0.0.1', port=5000, debug=True, use_debugger=False, use_reloader=False)