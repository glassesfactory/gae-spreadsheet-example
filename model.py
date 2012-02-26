#!/usr/bin/env python
# -*- cofing: utf-8 -*-

import gdata.spreadsheet.service

class ArticleModel():
	dbClient = None
	spread_id = ''
	sheet_id = ''

	def __init__(self):
		user = 'アカウントID'
		passwd = 'パスワード'
		self.dbClient = gdata.spreadsheet.service.SpreadsheetsService(user, passwd)
		self.dbClient.ProgrammaticLogin()

		q = gdata.spreadsheet.service.ListQuery()
		q['title'] = 'スプレッドシート名、ワークシート名'
		feed = self.dbClient.GetSpreadsheetsFeed(query=q)
		self.spread_id = feed.entry[0].id.text.rsplit('/',1)[1]
		feed = self.dbClient.GetWorksheetsFeed(self.spread_id)
		self.sheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

	"""
	モサッと取る
	"""
	def getFeed(self):
		return self.dbClient.GetListFeed(self.spread_id,self.sheet_id).entry

	"""
	指定した件数のレコードを取得
	"""
	def getFeedWithRange(self, start_index=1, max_results=None):
		q = gdata.spreadsheet.service.ListQuery()
		q.start_index = start_index
		if max_rows != None:
			q.max_results = max_results
		return self.dbClient.GetListFeed(self.spread_id,self.sheet_id, query=q).entry
		
	"""
	単一レコードを取得
	"""
	def getRecord(self, id):
		q = gdata.spreadsheet.service.ListQuery()
		q.sq = 'id == %s' % id
		return self.dbClient.GetListFeed(self.spread_id,self.sheet_id, query=q).entry