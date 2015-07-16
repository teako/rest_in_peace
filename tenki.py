# -*- coding: utf-8 -*-
#! /usr/bin/env python

from urllib import request
from xml.dom import minidom
from html.parser import HTMLParser, HTMLParseError
from urllib import parse



tenki = "http://www.drk7.jp/weather/xml/17.xml"
kion = "http://www.jma.go.jp/jp/amedas_h/today-56146.html?areaCode=000&groupCode=41"

urlopen = request.urlopen(tenki).read()
open2 = urlopen.decode("utf-8")
doc = minidom.parseString(open2)
area = doc.getElementsByTagName("area")
noto = next(filter(lambda x:x.getAttribute("id") == "能登", area), None) 

#kion
file = request.urlopen(kion).read()
file2 = file.decode("utf-8")
x = 0
y = 0
z = 0
w = ""

class Resultparser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        global x
        global y
        global z
        if "td" == tag and "class" in attrs and attrs["class"] == "time left" :
            x = 10
        if "td" == tag and "class" in attrs and attrs["class"] == "block middle" and z == 10:
            y = 10

    def handle_data(self, data):
        global x
        global y
        global z
        global w
        if x == 10 and data == "7":
            z = 10
        if x == 10 and y == 10 and z == 10:
            w = data
            x = 0
            y = 0
            z = 0
            
result = Resultparser()
result.feed(file2)
result.close()


print( "今日の能登地方の天気は「" + (noto.getElementsByTagName("weather")[0].childNodes[0].data) + "」、七尾市の７時現在の気温は" + w +"℃である！")


