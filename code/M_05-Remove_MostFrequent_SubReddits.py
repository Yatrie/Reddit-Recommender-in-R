'''
Module to drop records with comments tying to top 75-100 hand curated subReddits

Source for top SubReddits: http://redditlist.com/

@author: Vivek M Agrawal (vagrawal39@gatech.edu)
'''

import json
import os
import csv
import time

print 'DROPPING RECORDS WITH COMMENTS TIED TO TOP-100 SUBREDDITS...'

print 'Started processing at: ' + str(time.ctime())

# store the user and subreddit in a dictionary
# user: [subreddit,subreddit,... subreddit]
userSR = {}

with open('output\userSR_nonProfane.json', 'r') as json_file:
    for line in json_file:
        json_data = json.loads(line)
        userSR.update(json_data)

print 'Before dropping users with ONLY generic SubReddit contributions, the count was: ' + str(len(userSR))

with open('top_subReddits', 'rb') as data_file:
    for line in data_file:
        topSR = frozenset(line.lower().split(','))

counter = 0

matchedSR = []

for key in userSR.keys():
    counter += 1
    sR = frozenset([x.lower() for x in userSR[key]]).difference(topSR)
    #print userSR[key], sR, len(sR)
    if len(sR) < 2:
        del userSR[key]
    else:
        userSR[key] = list(sR)
        matchedSR.append(list(sR))
        #print userSR[key]
    #if counter%50000 == 0:
        #print 'processed another 50K'

print 'After dropping users with ONLY generic SubReddit contributions, the count was: ' + str(len(userSR))

with open('output\userSR_topSR.json', 'w') as fp_subReddit:
    json.dump(userSR, fp_subReddit)

# store all remaining records as well...
with open('output\matchedSR.csv', 'wb') as fp_matchedSR:
    writer = csv.writer(fp_matchedSR)
    writer.writerows(matchedSR)

print 'Ended processing at: ' + str(time.ctime())
