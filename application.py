#!/usr/bin/env python
# -*- cofing: utf-8 -*-
from flask import Flask
import filters

from view import MainView

app = Flask(__name__)
app.jinja_env.filters['mb_truncate'] = filters.mb_truncate

view = MainView()

@app.route('/')
def index():
	return view.list()

@app.route('/article/<int:id>')
def show(id):
	return view.show(id)

if __name__ == '__main__':
	app.run()