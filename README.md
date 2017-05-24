# Instructions:

We've prepared a small script running in container which tries to query a database with specific table and columns and display it through web interface.
You're work is to launch a mysql-database, create a database (you can pick the name), create a table named `employees` with the structure detailed below.
Insert a row filling all the columns with what ever you want, the only thing you must do is set id = 1.

Once you've done this you'll need to build an image from the Dockerfile we've prepared for you and run it in the background while providing the relevant environment variables to your mysql database and exposing the web interface port (5000) to some external port.
The available environment variables to use are listed below.

If you've managed to do this successfully you shoudl be able to browse your docker-machine ip with the external port and get a nice hello message.






### Table structure:

 - `id` - int
 - `first_name` string/varchar
 - `last_name` string/varchar
 - `age` int

### SQL Query to create the table:
`CREATE TABLE employees (id INT(20), first_name VARCHAR(30), last_name VARCHAR(30), age INT(3));`

### Container gets the following environment variables:
 - `DB_HOST` - MySQL database host ip
 - `DB_USER` - MySQL user
 - `DB_PASS` - MySQL password
 - `DB_NAME` - MySQL database name
