'''
Module to identify user - objectionable SubReddits combinations from the Reddit comments data

@author: Vivek M Agrawal (vagrawal39@gatech.edu)
'''

import json
import os
import csv
import time

print 'REMOVING RECORDS OF OBSCENE SUBREDDITS FROM THE COMMENTS DATABASE'

# store the user and subreddit in a dictionary
# user: [subreddit,subreddit,... subreddit]
userSR = {}

print 'Started processing at: ' + str(time.ctime())

with open('output\userSR.json', 'r') as json_file:
    for line in json_file:
        json_data = json.loads(line)
        userSR.update(json_data)

print 'Count of User-SubReddit Combinations in the input before Obscenity Filtering: ' + str(len(userSR))

with open('output\profane_subReddits', 'rb') as data_file:
    for line in data_file:
        badWords = frozenset(line.lower().split(','))

counter = 0

for key in userSR.keys():
    counter += 1
    sR = frozenset([x.lower() for x in userSR[key]])
    if sR.intersection(badWords):
        #print 'deleting ' + str(key)
        del userSR[key]
    #if counter%50000 == 0:
        #print 'processed another 50K'

print 'Count of User-SubReddit Combinations in the output after Obscenity Filtering: ' + str(len(userSR.keys()))

with open('output\userSR_nonProfane.json', 'w') as fp_subReddit:
    json.dump(userSR, fp_subReddit)

print 'Ended processing at: ' + str(time.ctime())
