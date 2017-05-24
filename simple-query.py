#!/usr/bin/env python

import _mysql
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    db = _mysql.connect(host=os.environ.get('DB_HOST'), user=os.environ.get('DB_USER'), passwd=os.environ.get('DB_PASS'), db=os.environ.get('DB_NAME'))

    db.query("""SELECT first_name, last_name, age FROM employees
             WHERE id = 1""")

    results = db.store_result()
    row = results.fetch_row(how=1)[0]

    return "<h1>Hey {} {} - You're {} years old!</h1>".format(row['first_name'], row['last_name'], row['age'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
