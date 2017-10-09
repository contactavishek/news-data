#! /usr/bin/env  python3
# PROJECT: LOGS ANALYSIS

import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


def get_report1():
    # 1. What are the most popular three articles of all time
    #    Executing 1st Query    
        c.execute("select title as article, count(*) as views "
                  "from articles join log "
                  "on concat('/article/',articles.slug)=log.path "
                  "group by articles.title "
                  "order by views desc limit 3")
        result1 = c.fetchall()
        print "\nMost popular 3 articles of all time:-\n"
        for i in range(0, len(result1), 1):
            print "\"" + result1[i][0] + "\" - " + \
              str(result1[i][1]) + " views"


def get_report2():
    # 2. Who are the most article popular authors of all time
    #    Executing 2nd Query
        c.execute("select authors.name, count(*) as views "
                  "from authors inner join articles "
                  "on authors.id = articles.author "
                  "inner join log on "
                  "concat('/article/',articles.slug)=log.path "
                  "group by authors.name "
                  "order by views desc")
        result2 = c.fetchall()
        print "\nMost popular article authors of all time:-\n"
        for i in range(0, len(result2), 1):
            print "\"" + result2[i][0] + "\" - " + \
              str(result2[i][1]) + " views"

         
def get_report3():
    # 3. On which days did more than 1% of requests lead to errors
    #    Executing 3rd Query from views created in database 'news'
        c.execute("select total_request.day, "
                  "round((error_request.errors*100.00)/ "
                  "total_request.total_errors,2) "
                  "as Percentage_requests from "
                  "error_request join total_request "
                  "on error_request.day=total_request.day "
                  "where round((error_request.errors*100.00)/ "
                  "total_request.total_errors,2)>1.00")
        result3 = c.fetchall()
        print "\nDays on which more than 1% of requests lead to errors:-\n"
        for i in range(0, len(result3), 1):
            print "\"" + str(result3[i][0]) + "\" - " + \
              str(result3[i][1]) + "% errors"


get_report1()
get_report2()
get_report3()
db.close()

