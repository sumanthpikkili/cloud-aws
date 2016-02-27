# Author Name: Sumanth Pikkili
# UTA ID: 1001100941
# CSE 6331 - 002: Cloud Computing
# Assignment 2 - AWS
# References: 
# https://devcenter.heroku.com/articles/s3-upload-python
# http://boto.readthedocs.org/en/latest/s3_tut.html
# http://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto

import boto
import boto.s3
import sys
from boto.s3.key import Key
import time

# Obtaining the AWS Access and secret keys from the user

AWS_ACCESS_KEY_ID = raw_input("Enter the Access Key")
AWS_SECRET_ACCESS_KEY = raw_input("Enter the Secret Key")

# Connecting to S3

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket_name='awsassignment2'

# Creating a Bucket

bucket = conn.create_bucket(bucket_name,location=boto.s3.connection.Location.DEFAULT)

#Getting the File to Upload

testfile='all_month.csv'
print 'Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

k = Key(bucket)
k.key = 'all_month.csv'

starttime=time.time()
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)
endtime=time.time()

# Calculating the Time taken to upload the file to S3
print "Time taken to upload to S3 is",endtime-starttime,"seconds"
