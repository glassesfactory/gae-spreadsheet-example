#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request
import gdata.spreadsheet.text_db

from model import ArticleModel

class MainView():
	model = None
	def __init__(self):
		self.model = ArticleModel()
		
	"""
	とりあえず CRUD っぽく作っとくよ
	"""
	def list(self):
		rows = self.model.getFeed()
		articles = []
		for entry in rows:
			article = gdata.spreadsheet.text_db.Record(row_entry=entry)
			articles.append(article.content)

		if "X-PJAX" in request.headers:
			return render_template('index-p.html', articles=articles)
		else:
			return render_template('index.html', articles=articles)

	def show(self,id):
		records = self.model.getRecord(id)
		article = gdata.spreadsheet.text_db.Record(row_entry=records[0]).content
		if "X-PJAX" in request.headers:
			return render_template('show-p.html',article=article)
		else:
			return render_template('show.html', article=article)