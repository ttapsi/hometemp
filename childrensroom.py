#!/usr/bin/python

import MySQLdb
import sys
import gc
import os
import ConfigParser

def header():
   print '-------------------------------------------------'
   print '\tDATE\t\tTEMPERATURE\tHUMIDITY'
   print '-------------------------------------------------'


print '\n--- childrensroom -------------------------------'

sql = 'SELECT date,temperature, humidity FROM childroom ORDER BY date DESC '
if len(sys.argv) == 2 :
   sql += 'LIMIT ' +  str(sys.argv[1])
elif len(sys.argv) == 3 :
   sql += 'LIMIT ' +  str(sys.argv[1]) + ' OFFSET ' + str(sys.argv[2])

try:
   config = ConfigParser.RawConfigParser()
   config.read(os.path.dirname(os.path.realpath(__file__)) + '/temperature.properties')
   db = MySQLdb.connect(config.get('mysql', 'server'),config.get('mysql', 'user'),config.get('mysql', 'password'), config.get('mysql', 'database') )
   cursor = db.cursor()

   cursor.execute(sql)
   data = cursor.fetchall()
   
   counter = 0
   for row in data :
      if counter % 20 == 0:
         header()
      print row[0],'\t{0:0.1f}*C\t\t{1:0.1f}%'.format(row[1],row[2])
      counter += 1

except Exception, e:
   print repr(e)

print '\n'
db.close()
gc.collect()
