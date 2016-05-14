#!/usr/bin/python

import Adafruit_DHT
import MySQLdb
import sys
import os
import ConfigParser

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

# example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# humidity = 50.0
# temperature = 22.4

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!
if humidity is not None and temperature is not None:
	# Open database connection
	config = ConfigParser.RawConfigParser()
        config.read(os.path.dirname(os.path.realpath(__file__)) + '/temperature.properties')
        db = MySQLdb.connect(config.get('mysql', 'server'),config.get('mysql', 'user'),config.get('mysql', 'password'), config.get('mysql', 'database') )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO childroom  (date,temperature,humidity) VALUES (NOW(), '{0:0.1f}', '{1:0.1f}' )".format(temperature,humidity)
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
