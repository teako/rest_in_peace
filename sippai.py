# -*- coding: utf-8 -*-
#! /usr/bin/env python
from xml.etree.ElementTree import *
from urllib import request
from xml.dom import minidom
 
tenki = "http://www.drk7.jp/weather/xml/17.xml"

urlopen = request.urlopen(tenki).read()
open2 = urlopen.decode("utf-8")
doc = minidom.parseString(open2)
tenkis = doc.getElementsByTagName("weather")[7].childNodes[0].data
print (tenkis)
#print(open2)
#print(tenkis.data)
