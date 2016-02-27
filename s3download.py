#AUTHOR Name: Sumanth Pikkili
# UTA ID: 1001100941
# CSE 6331-002 Cloud Computing
# Assignment 2 - AWS
# References
# http://www.laurentluce.com/posts/upload-and-download-files-tofrom-amazon-s3-using-pythondjango/


import boto
import os,sys
from boto.s3.key import Key
import time

#Getting the Access Key and the Secret Key from the user
AWS_ACCESS_KEY_ID = raw_input("Enter the Access Key")
AWS_SECRET_ACCESS_KEY = raw_input("Enter the Secret Access Key")

#Setting the local path in the file
LOCAL_PATH=''
bucket_name='awsassignment2'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)

bucket_list = bucket.list()
l=Key(bucket)

filename=raw_input("Enter the filename to be downloaded from S3 bucket awsassignment2")
l.key=filename

# check if file exists locally, if not: download it

starttime=time.time()

if not os.path.exists('all_month.csv'):	
	l.get_contents_to_filename(l.key)

endtime=time.time()
print "The time taken to download from S3 to local is",endtime-starttime,"seconds"
