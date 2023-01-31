"""
Freddy Lopez's Flask API.
"""

from flask import Flask, abort, send_from_directory, render_template, request
import os 
from os import path
import configparser
import logging

app = Flask(__name__)

@app.route("/<path:request>")
    
def hello(request):
    print(request)
    cwd = os.getcwd()
    print(cwd)
    ncwd = cwd + "/pages" + "/"+request

    if "~" in request or ".." in request:
        abort(403)

    elif path.exists(ncwd) == False:
        abort(404)

    elif path.exists(ncwd):
        return send_from_directory('pages/', request), 200
        
    # abort(403)
    # abort(404)
    '''return send_from_directory("hello.html")'''


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def file_not_found(e):
    return send_from_directory('pages/', '404.html'), 404


def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config
if __name__ == "__main__":
    config  = parse_config(["credentials.ini", "default.ini"])
    port1 = config["SERVER"]["PORT"]
    debug1 = config["SERVER"]["DEBUG"]
    app.run(debug=debug1, host='0.0.0.0', port=port1)


