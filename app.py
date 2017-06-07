#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, traceback, configparser, os
from flask import Flask
app = Flask(__name__)


# start configuration parser
parser = configparser.ConfigParser()
parser.read("app.conf")

# reading variables
logger_level = parser.get('logging', 'logger_level', raw = True)
handler_level = parser.get('logging', 'handler_level', raw = True)
log_format = parser.get('logging', 'log_format', raw = True)
log_file = parser.get('logging', 'log_file')

# set logger logging level
logger = logging.getLogger(__name__)
logger.setLevel(eval(logger_level))

# set handler logging level
handler = logging.FileHandler(log_file)
handler.setLevel(eval(handler_level))

# create a logging format
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
