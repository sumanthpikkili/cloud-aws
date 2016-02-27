# cloud-aws
AWS S3, EC2, RDS

##DESCRIPTION
 Upload a large csv file to the S3 bucket, copy the file from S3 to the EC2 instance, extract it to the AWS relational database (RDS) and find the time magnitude relationship i.e the most frequent and the least frequent earthquakes that occurred in the past 30 days. Fire 2000 random queries to the RDS database and compare the execution times of query results retrieved via Memcache.

## TECHNICAL SPECIFICATIONS
    Platform: MAC OSX Yosemite (32 bit) Language Used: Python
    AWS Products Used: S3, EC2, RDS Tool Used: MAC terminal
    Python Modules imported: boto, MySQLdb, memcache

##STEPS PERFORMED AND RESULTS OBTAINED
###STEP 1:
The file with earthquakes’ details (all_month.csv) was initially downloaded manually from the web site http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php and saved on the local machine. It was placed in the AWS Cloud Folder (On the Desktop)

##STEP 2:
An AWS account was created and an EC2 instance (Ubuntu) was created. AWS CLI was installed on the local machine.
STEP 3:
The ‘awscloud1.py’ program(In the ZIP file) uploads the csv file from the AWS Cloud Folder to S3. The Python code creates a bucket in AWS S3 and places the file there. The time taken to upload the file ‘all_month.csv’ to S3 was 0.657 seconds.

##STEP 3:
The ‘awscloud1.py’ program(In the ZIP file) uploads the csv file from the AWS Cloud Folder to S3. The Python code creates a bucket in AWS S3 and places the file there. The time taken to upload the file ‘all_month.csv’ to S3 was 0.657 seconds.
￼￼￼￼￼
##￼STEP 4:
￼Connect to the AWS EC2 instance
Downloaded the .pem file to the AWS Cloud Folder and ran the following commands: chmod 400 awsec2keypair.pem.txt
ssh -i awsec2keypair.pem.txt ubuntu@ec2-52-11-6-38.us-west-2.compute.amazonaws.com

##STEP 5:
Copy the File from S3 to EC2
The file ‘all_month.csv’ was copied from S3 to EC2 using the following command: aws s3 cp s3://bucket/awsassignment/all_month.csv all_monthcopied.csv

##STEP 6:
An RDS Instance was created. MySQL was installed on EC2 and the following command was used to connect to mysql RDS.
sudo mysql -h sumanthdbinstance.cag6cgdcyy5y.us-west-2.rds.amazonaws.com -P 3306 -u sumanthpikkili -p sumanthpikkilidb
￼￼￼￼￼
##￼STEP 7:
A table was created in RDS.
CREATE TABLE quakes ( datetime TIMESTAMP NOT NULL, latitude DECIMAL(10,8) NOT NULL, longitude DECIMAL(10,8) NOT NULL, depth DECIMAL(5,2) NOT NULL, mag DECIMAL(3,2) NOT NULL, magtype VARCHAR(10) NOT NULL, nst INTEGER(5), gap INTEGER(5), dmin DECIMAL(14,1), rms DECIMAL(3,2), net VARCHAR(3), id VARCHAR(15), updated TIMESTAMP NOT NULL, location VARCHAR(45) NOT NULL, type VARCHAR(10), PRIMARY KEY (id) );
The following command was used to export the csv file to RDS.
load data local infile 'all_monthcopied.csv' into table quakes fields terminated by ',' enclosed by '"' lines terminated by
'\n' (datetime,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,location,type) ;
￼￼
##STEP 8:
￼Ran the Python program ‘rds.py’(In the ZIP file). This gives the time magnitude relationship i.e the most frequent and the least frequent earthquakes that occurred in the past 30 days.It also calculates the query times for 2000 random queries and 2000 random queries with limited scope(Without Memcache).Time taken for executing 2000 random queries is 476.249 seconds. Time taken for executing 2000 random queries with limited scope is 399.67 seconds.
