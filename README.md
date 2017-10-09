
                       LOGS ANALYSIS PROJECT

Introduction

This is a python module that uses information from the database of a web server and draws conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The database includes three tables:

•	The authors table includes information about the authors of articles.
•	The articles table includes the articles themselves.
•	The log table includes one entry for each time a user has accessed the site.

The reporting tool needed to answer the following questions:

1. Most popular three articles of all time.
2. Most popular article authors of all time.
3. Days on which more than 1% of requests lead to errors.


Views Need To Be Created in ‘news’ Database:

Views were used only for question 3 to break the problem down to understand it easier.

Creating VIEW error_request in ‘news’ database

create view error_request as
select date(time) as day, count(status) as errors
from log where status! = ’200 OK’
group by day
order by errors;

Creating VIEW total_request in ‘news’ database

create view total_request as
select date(time) as day, count(status) as total_errors
from log
group by day
order by total_errors;


Running the code

These instructions assume you have the Udacity provided FSND Virtual machine and Udacity provided ‘news’ database:

•	Make sure you have newsdata.sql, the SQL script file with all the data. The newsdata.zip file can be downloaded or cloned from this     repository.

•	Then run the following command to execute it in ‘news’ database. You might have to create the ‘news’ database before-hand if it         doesn’t exist : psql -d news -f newsdata.sql

•	Connect to the psql database with: psql -d news

•	Create views for the database (mentioned above)

•	Finally run the script:  python logs_analysis.py

•	It will present you with necessary reports.

