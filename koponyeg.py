#!/usr/bin/python

import MySQLdb
import sys
import gc
import urllib
import urllib
from lxml import html

url = "http://koponyeg.hu/t/Pilisborosjeno"
page = html.fromstring(urllib.urlopen(url).read())

link = page.xpath("//div[@id='temperature_text']")[0]
print link.text.strip()[:-2]
link = page.xpath("//div[@id='act_humidity']")[0]
print link.text.strip()[:-1]

	#print "Name", link.text, "URL", link.get("href")

#def header():
#   print '-------------------------------------------------'
#   print '\tDATE\t\tTEMPERATURE\tHUMIDITY'
#   print '-------------------------------------------------'


#print '\n--- workroom ------------------------------------'



#sql = 'SELECT date,temperature, humidity FROM workroom ORDER BY date DESC '
#if len(sys.argv) == 2 :
#   sql += 'LIMIT ' +  str(sys.argv[1])
#elif len(sys.argv) == 3 :
#   sql += 'LIMIT ' +  str(sys.argv[1]) + ' OFFSET ' + str(sys.argv[2])

#try:
#   db = MySQLdb.connect("localhost","temperature","Gatya01","temperature" )
#   cursor = db.cursor()

#   cursor.execute(sql)
#   data = cursor.fetchall()
   
#   counter = 0
#   for row in data :
#      if counter % 20 == 0:
#         header()
#      print row[0],'\t{0:0.1f}*C\t\t{1:0.1f}%'.format(row[1],row[2])
#      counter += 1

#except Exception, e:
#   print repr(e)

#print '\n'
#db.close()
#gc.collect()
