# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import flask
from flask import Flask, request
from . import main

app = flask.Flask(__name__)


autocomplete_instance = main.Autocomplete()

@app.route('/')
def home():
    return 'Autocomplete service'

@app.route("/search")
def search():
    query = request.args.get("word", "")
    if not query:
        flask.abort(404)

    results = autocomplete_instance.find_autocomplete_answers(query, max_results=25)

    return flask.jsonify(results)

