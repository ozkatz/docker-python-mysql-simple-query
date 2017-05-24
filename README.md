# Instructions:

We've prepared a small script running in container which tries to query a database with specific table and columns.
You're work is to launch a mysql-database, create a database (you can pick the name), create a table named employees with the structure detailed below.
Insert a row filling all the columns with what ever you want, the only thing you must do is set id = 1.

Once you've done this you'll need to build an image from the Dockerfile we've prepared providing the relevant environment variables to your mysql host,
the available environment variables to use are listed below.

If you've managed to do this successfully you should get a nice hello message.








### Table structure:

 - `id` - int
 - `first_name` string/varchar
 - `last_name` string/varchar
 - `age` int

### Container gets the following environment variables:
 - `DB_HOST` - MySQL database host ip
 - `DB_USER` - MySQL user
 - `DB_PASS` - MySQL password
 - `DB_NAME` - MySQL database name
