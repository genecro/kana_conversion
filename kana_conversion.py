# -*- coding: UTF-8 -*-

def hira2Kata(hiragana):
	hiragana = hiragana.decode('utf-8')
	katakana = ""
	for kana in hiragana:
		if ord(kana) >= ord("ぁ".decode('utf-8')) and ord(kana) <= ord("ゖ".decode('utf-8')):
			katakana += unichr(ord(kana) + ord(u'\u0060'))
		else:
			katakana += kana
	return katakana

def kata2Hira(katakana):
	katakana = katakana.decode('utf-8')
	hiragana = ""
	for kana in katakana:
		if ord(kana) >= ord("ァ".decode('utf-8')) and ord(kana) <= ord("ヶ".decode('utf-8')):
			hiragana += unichr(ord(kana) - ord(u'\u0060'))
		else:
			hiragana += kana
	return hiragana
