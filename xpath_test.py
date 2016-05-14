#!/usr/bin/python

import Adafruit_DHT
import MySQLdb
import sys
import urllib
from lxml import html

url = "http://koponyeg.hu/t/Pilisborosjeno"
page = html.fromstring(urllib.urlopen(url).read())

link = page.xpath("//div[@id='temperature_text']")[0]
print  link.text.strip()[:-2]
link = page.xpath("//div[@id='act_humidity']")[0]
print link.text.strip()[:-1]
link = page.xpath("//div[@class='actual_inline']//img/@class")[0]
print link[link.rfind(' '):].strip().replace('--','-')
link = page.xpath("//div[@id='act_sunset']")[0]
print link.text.strip()
link = page.xpath("//div[@id='act_sunrise']")[0]
print link.text.strip()
link = page.xpath("//div[@id='act_pressure']")[0]
print link.text.strip()
link = page.xpath("//div[@id='act_wind']")[0]
print link.text.strip()
link = page.xpath("//*[@id='grafikon_15napos']/div[6]/img/@alt")[0]
print link
link = page.xpath("//*[@id='grafikon_15napos']/div[7]/img/@alt")[0]
print link

#link = page.xpath("//div[@id='act_moon']/div/following-sibling")
#print link.text


