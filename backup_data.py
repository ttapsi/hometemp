#!/usr/bin/python

import os
import ConfigParser
import time

config = ConfigParser.RawConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__)) + '/temperature.properties')

server=config.get('mysql', 'server')
user=config.get('mysql', 'user')
password=config.get('mysql', 'password')
database=config.get('mysql', 'database')
date=time.strftime("%Y-%m-%d")
filename="""temperature_backup_{0}.sql""".format(date)

os.system("""mysqldump -u{0} -p{1} -h{2} {3} > {4}""".format(user, password, server, database, filename))
os.system("gzip " + filename );
os.system("""cp {0}.gz /share/home/mysql""".format(filename))

os.system("""rm {0}.gz""".format(filename))
