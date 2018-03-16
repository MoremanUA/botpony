import requests, datetime 
import sys, re
import lxml.html, cssselect

class myHelp:
     def __init__ (self):
         self.mText ='1.team(состав) - основной состав команды;\n\
2.games - ближайшее игры;\n3.anagram(анаграм) *word - Анаграмайзер для слово *word'

class myFunctions:
    def __init__(self):
        self.anag_url = "http://www.anagramizer.com/find-anagram"

    def anagramizer(self, word):
        url = self.anag_url + '?word='+word
        resp = requests.get(url)
        parsed = lxml.html.fromstring(resp.text)
        res =  parsed.cssselect('ul li b')
        result = ''
        for i in res:
            result += "-"+i.text+"\n"
        return result


