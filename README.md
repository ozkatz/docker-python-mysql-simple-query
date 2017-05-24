# Instructions:

We've prepared a small script running in container which tries to query a database with specific table and columns and display it through a web interface.
Your job is to take a plain CentOS 7 box (could be on Vagrant, AWS, GCE, or any other provider you'd like), and provision it with the following components:

1. A MySQL server - You'll need to have mysqld running on the machine. The web application will use it to retrieve data
2. A MySQL database - You'll need to have a database created on your MySQL server. Feel free to give it any name you want
3. A MySQL table - Within our newly created database, we'll need to create a table using the structure given below
4. A Docker daemon - We will use it to launch a container running our web application
4. Our web application - A running instance of the web application. You can create a Docker image using the included dockerfile.

A few guildelines:

1. The web application should run as a Docker container on our machine. We'll need some mechanism to ensure it is always up, in case of a crash.
2. All steps need to be repeatable. We want to be able to spin up another machine with the exact same setup without manual intervention.
3. Since the web application needs to know the details of our MySQL instance, we'll need to pass a few environment variables as listed below.
4. The web app is exposed inside the container on port 5000. We'll want to expose the same port number on the machine, and have it route the traffic to the running container.
5. If everything is setup correctly, you should be able to surf to your new web app using `http://<host IP>:5000/` and get a nice hello message.
6. Your answer should be presented in the form of a git repo (either on Github or whatever else you'd like). It should contain a README file describing how to run the code on a clean CentOS machine.


### Table structure:

 - `id` - int
 - `first_name` string/varchar
 - `last_name` string/varchar
 - `age` int

### SQL Query to create the table:
```
CREATE TABLE employees (id INT(20), first_name VARCHAR(30), last_name VARCHAR(30), age INT(3));
```
Once the table is created, insert a single row with id = 1. Fill in the rest of the fields to your liking.


### Environment Variables for our web app
 - `DB_HOST` - MySQL server hostname or IP address
 - `DB_USER` - MySQL connection username
 - `DB_PASS` - MySQL password
 - `DB_NAME` - MySQL database name
 

