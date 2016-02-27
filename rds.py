# Author Name : Sumanth Pikkili
# UTA ID: 1001100941
# CSE 6331-002 - Cloud Computing
# Assignment 2 - AWS
# References: 
# http://stackoverflow.com/questions/18595490/connecting-to-mysql-db-on-rds
# http://boto.readthedocs.org/en/latest/rds_tut.html

import boto.rds
from time import sleep
import MySQLdb
import time
from array import array
from random import randint

# Get the AWS Access Key and the Secret Key from the user
ACCESS_KEY = raw_input("Enter the Access Key")
SECRET_KEY = raw_input("Enter the Secret Key")
USERNAME = "sumanthpikkili"
PASSWORD = "sumanthpikkili"
DB_PORT = 3306
DB_NAME = 'sumanthpikkilidb'

#Connecting to RDS Instance

conn = MySQLdb.connect(host="sumanthdbinstance.cag6cgdcyy5y.us-west-2.rds.amazonaws.com",user=USERNAME,passwd=PASSWORD,db=DB_NAME,port=3306)
print "Connected to RDS Instance"

cursor=conn.cursor()


#QUERY 1:  Number of Earthquakes with magnitude between 2 and 3 that occured in the past 30 days

query1="select count(*) from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 2 AND 3;"
cursor.execute(query1);
count_mag_2=cursor.fetchone();

#QUERY 2: Number of earthquakes that occured with  magnitude between 3 and 4 in the past 30 days

query2="select count(*) from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 3 AND 4;"
cursor.execute(query2);
count_mag_3=cursor.fetchone();

#Query 3: Number of earthquakes with magnitudes between 4 and 5 in the past 30 days

query3="select count(*) from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 4 AND 5;"
cursor.execute(query3);
count_mag_4=cursor.fetchone();

# Query 4: Number of earthquakes with magnitude greater than 5 in the past 30 days

query4="select count(*) from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag>5;"
cursor.execute(query4);
count_mag_5=cursor.fetchone();


arr_mag_counts=[count_mag_2,count_mag_3,count_mag_4,count_mag_5]

#Finding out the magnitude range of the most frequent earthquakes
if max(arr_mag_counts)==count_mag_2:
	print "Earthquakes with magnitudes between 2 and 3 have been the most frequent in the past 30 days"
elif max(arr_mag_counts)==count_mag_3:
	print "Earthquakes with magnitudes between 3 and 4 have been the most frequent in the past 30 days"
elif max(arr_mag_counts)==count_mag_4:
	print "Earthquakes with magnitudes between 4 and 5 have been the most frequent in the past 30 days"
else:
	print "Earthquakes with magnitudes greater than 5 have been the most frequent in the past 30 days"

#Finding out the magnitude range of the least frequent earthquakes
if min(arr_mag_counts)==count_mag_2:
        print "Earthquakes with magnitudes between 2 and 3 have been the least frequent in the past 30 days"
elif max(arr_mag_counts)==count_mag_3:
        print "Earthquakes with magnitudes between 3 and 4 have been the least frequent in the past 30 days"
elif max(arr_mag_counts)==count_mag_4:
        print "Earthquakes with magnitudes between 4 and 5 have been the least frequent in the past 30 days"
else:
        print "Earthquakes with magnitudes greater than 5 have been the least frequent in the past 30 days"


#QUERY 5:    Places where earthquakes occured more than 50 times

query5="select datetime as dateofoccurence,depth,mag as magnitude,location,count(*) c from earthquakes group by location having c>50;"	

 
#QUERY 6: Finding the regions where the depth of the earthquake is less than 1

query6="select datetime,depth,mag,location from earthquakes where depth<1;"

quakesarray=(query1,query2,query3,query4,query5,query6)


starttime=time.time()
for x in range(1,2000):

	random_number=randint(0,5)
	cursor.execute(quakesarray[random_number])

endtime=time.time()
print "Time taken for executing 2000 random queries is:",endtime-starttime,"Seconds"



# LIMITED SCOPE - LIMIT 2000

#QUERY 1 Limited Scope: Earthquakes with magnitude between 2 and 3 that occured in the past 30 days

query1_ls="select location,depth,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 2 AND 3 limit 2000;"

#QUERY 2 Limited Scope: Earthquakes that occured with  magnitude between 3 and 4 in the past 30 days

query2_ls="select location,depth,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 3 AND 4 limit 2000;"


#Query 3 Limited Scope: Earthquakes with magnitudes between 4 and 5 in the past 30 days

query3_ls="select location,depth,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag BETWEEN 4 AND 5 limit 2000;"

# Query 4 Limited Scope: Earthquakes with magnitude greater than 5 in the past 30 days

query4_ls="select location,depth,mag from earthquakes where datetime between DATE_SUB(NOW(),INTERVAL 30 DAY)AND NOW() AND mag>5 limit 2000;"

quakesarray_ls=(query1_ls,query2_ls,query3_ls,query4_ls)

#Caluculating the time elapsed to execute 2000 queries with limited scope
starttime_ls=time.time()
for y in range(1,2000):

        random_number_ls=randint(0,3)
        cursor.execute(quakesarray_ls[random_number_ls])

endtime_ls=time.time()
print "Time taken for executing 2000 random queries with limited set of tuples is:",endtime_ls-starttime_ls,"Seconds"














