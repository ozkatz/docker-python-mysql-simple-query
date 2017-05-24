#!/usr/bin/env python

import _mysql
import os

db = _mysql.connect(host=os.environ.get('DB_HOST'), user=os.environ.get('DB_USER'), passwd=os.environ.get('DB_PASS'), db=os.environ.get('DB_NAME'))

db.query("""SELECT first_name, last_name, age FROM employees
         WHERE id = 1""")

results = db.store_result()
row = results.fetch_row(how=1)[0]

print "Hey {} {}, you're {} old!".format(row['first_name'], row['last_name'], row['age'])