'''
Module to parse the time series Reddit comments data in JSON format to extract relevant fields for association mining

@author: Vivek M Agrawal (vagrawal39@gatech.edu)

Requires Python 2.7

Note: Assumes the uncompressed Reddit Comments file is present in \input folder
'''

import json
import time
import csv

print 'PARSE RAW REDDIT DATA (JSON FORMATTED)...'

print 'Started processing at: ' + str(time.ctime()) 

# store only relevant comment fields in a csv structure
# 'id', 'author', 'subreddit', 'ups', len('body')
commentData = []

countFile = 1000;

#with open('RC_2015-05_100') as json_file:
with open('input\RC_2015-05_4850') as json_file:
    for line in json_file:
        # read json data
        json_data = json.loads(line)
        
        # create record for comment data, ignoring deleted users
        if json_data['author'] != "[deleted]":
            commentData.append([json_data['id'], json_data['author'], json_data['subreddit'], json_data['ups'], len(json_data['body'])])
        
        # clean the slate at every 1M record
        if len(commentData) > 1000000:
            with open(str('commentData_'+str(countFile)+'.csv'), 'wb') as fp_commentData:
                writer = csv.writer(fp_commentData)
                writer.writerows(commentData)
            
            # print time for 1M records
            print 'Processed 1M records in: ' + str(time.ctime())
            
            # release memory and restart
            del(commentData); commentData = []
            countFile += 1

# store all remaining records as well...
with open(str('output\commentData_'+str(countFile)+'.csv'), 'wb') as fp_commentData:
    writer = csv.writer(fp_commentData)
    writer.writerows(commentData)

print 'Finished processing at: ' + str(time.ctime())
