#!/usr/bin/python

import Adafruit_DHT
import MySQLdb
import sys
import os
import urllib
from lxml import html
import ConfigParser

url = "http://koponyeg.hu/t/Pilisborosjeno"
page = html.fromstring(urllib.urlopen(url).read())

link = page.xpath("//div[@id='temperature_text']")[0]
temperature = link.text.strip()[:-2]
link = page.xpath("//div[@id='act_humidity']")[0]
humidity = link.text.strip()[:-1]
link = page.xpath("//div[@class='actual_inline']//img/@class")[0]
css = link[link.rfind(' '):].strip().replace('--','-')
link = page.xpath("//div[@id='act_sunset']")[0]
sunrise = link.text.strip()
link = page.xpath("//div[@id='act_sunrise']")[0]
sunset = link.text.strip()
link = page.xpath("//div[@id='act_pressure']")[0]
pressure = link.text.strip()
link = page.xpath("//div[@id='act_wind']")[0]
wind = link.text.strip()
link = page.xpath("//*[@id='grafikon_15napos']/div[6]/img/@alt")[0]
maxtemp = link
link = page.xpath("//*[@id='grafikon_15napos']/div[7]/img/@alt")[0]
mintemp =  link

if humidity is not None and temperature is not None:
	# Open database connection
	config = ConfigParser.RawConfigParser()
	config.read(os.path.dirname(os.path.realpath(__file__)) + '/temperature.properties')
        db = MySQLdb.connect(config.get('mysql', 'server'),config.get('mysql', 'user'),config.get('mysql', 'password'), config.get('mysql', 'database') )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO weindorf (date,temperature,humidity,css,sunset,sunrise,pressure,wind,maxtemp,mintemp) 
		 VALUES (NOW(), '{0:0.1f}', '{1:0.1f}','{2}','{3}','{4}','{5}','{6}','{7:0.1f}','{8:0.1f}' 
		 )""".format(float(temperature),float(humidity),css,sunset,sunrise,pressure,wind,float(maxtemp),float(mintemp))
	# data = {"12.2", "25.6"}

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except Exception, e:
	   # Rollback in case there is any error
	   print repr(e)
	   db.rollback()
	
	# disconnect from server
	db.close()
else:
	print 'Failed to get reading. Try again!'
