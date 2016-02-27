# AUTHOR Name: Sumanth Pikkili
# UTA ID: 1001100941
# CSE6331-002 - Cloud Computing
# Assignment 2 - AWS


import memcache
from time import sleep
import MySQLdb
import time
import sys
from random import randint
#References:
# http://dev.mysql.com/doc/mysql-ha-scalability/en/ha-memcached-interfaces-python.html

USERNAME = "sumanthpikkili"
PASSWORD = "sumanthpikkili"
DB_PORT = 3306
DB_NAME = 'sumanthpikkilidb'

#Connecting to RDS Instance

conn = MySQLdb.connect(host="sumanthdbinstance.cag6cgdcyy5y.us-west-2.rds.amazonaws.com",user=USERNAME,passwd=PASSWORD,db=DB_NAME,port=3306)
print "Connected to RDS Instance"


# Creating the Memcached client

memc =memcache.Client(["127.0.0.1:11211"])

#Queries without limited scope
query1="select depth,location,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 2 AND 3;"
query2="select datetime,depth,mag,location from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 3 AND 4;"
query3="select datetime as dateofoccurence,depth,mag as magnitude,location,count(*) c from earthquakes group by location having c>50;"

# Flushing all the keys

memc.flush_all()

#Calculating the time for executing 2000 random queries
print "Calculating the time for executing 2000 random queries"

starttime=time.time()

for x in range(1,2000):
                random_number=randint(0,2)
                if random_number==0:

                        query_one=memc.get('query_one')
                        if not query_one:
                                cursor=conn.cursor()
                                cursor.execute(query1)
                                rows=cursor.fetchall()
                                memc.set('query_one',rows,2000)
                                print "Updated Memcached with Query 1 Results"
                        else:
                                print "Loaded Query 1 Results from Memcached"
                                for row in query_one:
                                        print "%s" %(row[0])

                elif random_number==1:
                        query_two=memc.get('query_two')
                        if not query_two:
                                cursor=conn.cursor()
                                cursor.execute(query2)
                                rows=cursor.fetchall()
                                memc.set('query_two',rows,2000)
                                print "Updated Memcached with Query 2 results"
                        else:
                                print "Loaded Query 2 results from Memcached"
                                for row in query_two:
                                        print "%s,%s,%s,%s" %(row[0],row[1],row[2],row[3])

                elif random_number==2:
                        query_three=memc.get('query_three')
                        if not query_three:
                                cursor=conn.cursor()
                                cursor.execute(query3)
                                rows=cursor.fetchall()
                                memc.set('query_three',rows,2000)
                                print "Updated Memcached with Query 3 Results"
                        else:
                                print "Loaded Query 3 results from Memcached"
                                for row in query_three:
                                        print "%s"%(row[0])


endtime=time.time()

#Queries with limited scope
query1_ls="select depth,location,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 2 AND 3 limit 2000;"
query2_ls="select datetime,depth,mag,location from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 3 AND 4 limit 2000;"
query3_ls="select datetime as dateofoccurence,depth,mag as magnitude,location,count(*) c from earthquakes group by location having c>50 limit 2000;"


#Calculating the time for executing 2000 random queries with limited scope
print "Calculating the time for executing 2000 random queries with limited scope"

starttime_ls=time.time()

for y in range(1,2000):
                random_number_ls=randint(0,2)
                if random_number_ls==0:

                        query_one_ls=memc.get('query_one_ls')
                        if not query_one_ls:
                                cursor_ls=conn.cursor()
                                cursor_ls.execute(query1_ls)
                                rows_ls=cursor_ls.fetchall()
                                memc.set('query_one_ls',rows_ls,2000)
                                print "Updated Memcached with Query 1 Results"
                        else:
                                print "Loaded Query 1 Results from Memcached"
                                for row in query_one_ls:
                                        print "%s" %(row[0])

                elif random_number_ls==1:
                        query_two_ls=memc.get('query_two_ls')
                        if not query_two_ls:
                                cursor_ls=conn.cursor()
                                cursor_ls.execute(query2_ls)
                                rows_ls=cursor_ls.fetchall()
                                memc.set('query_two_ls',rows_ls,2000)
                                print "Updated Memcached with Query 2 results"
                        else:
                                print "Loaded Query 2 results from Memcached"
                                for row in query_two_ls:
                                        print "%s,%s,%s,%s" %(row[0],row[1],row[2],row[3])

                elif random_number_ls==2:
                        query_three_ls=memc.get('query_three_ls')
                        if not query_three_ls:
                                cursor_ls=conn.cursor()
                                cursor_ls.execute(query3_ls)
                                rows_ls=cursor_ls.fetchall()
                                memc.set('query_three_ls',rows_ls,2000)
                                print "Updated Memcached with Query 3 Results"
                        else:
                                print "Loaded Query 3 results from Memcached"
                                for row in query_three_ls:
                                        print "%s"%(row[0])


endtime_ls=time.time()
print 'The time taken to run 2000 random queries is',endtime-starttime
print 'The time taken to run 2000 random queries with limited scope is',endtime_ls-starttime_ls

