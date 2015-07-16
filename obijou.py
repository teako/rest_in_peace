# -*- coding: utf-8 -*-
#! /usr/bin/env python

from html.parser import HTMLParser, HTMLParseError
from urllib import parse
from urllib import request

url = 'http://shindanmaker.com/514532'

postdic = {"u" : "七尾城", "from" : ""}
postdata = parse.urlencode(postdic).encode("utf-8")
file = request.urlopen(url, postdata).read()
file2 = file.decode("utf-8")
x = 0
y = 0

class Resultparser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        global x
        global y
        if "form" == tag and attrs["id"] == "forcopy" :
            x = 10
        if "textarea" == tag and x == 10:
            y = 10

    def handle_data(self, data):
        global x
        global y
        if x == 10 and y == 10 :
            print(data)
            x = 0
            y = 0


result = Resultparser()
result.feed(file2)
result.close()
