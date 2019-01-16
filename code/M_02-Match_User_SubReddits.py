'''
Module to condense the time series comments data to User - SubReddit correations

@author: Vivek M Agrawal (vagrawal39@gatech.edu)

Required Python 2.7
'''

import json
import os
import csv
import time

#path = r'C:\Users\Vivek\Desktop\Fall 2015\CS-8803 BD\Project\RC_2015-05\test'
path = os.getcwd() + '\\output'

# store the user and subreddit in a dictionary
# Format - Dict {user: [subreddit,subreddit,... subreddit]}
userSR = {}
subReddits = set();

print 'MATCHING USERS WITH SUBREDDITS...'

for dir_entry in os.listdir(path):
    print 'Started processing ' + str(dir_entry) + ' at: ' + str(time.ctime())
    # get the directory path name
    dir_entry_path = os.path.join(path, dir_entry)
    if os.path.isfile(dir_entry_path):
        with open(dir_entry_path, 'r') as data_file:
            for line in data_file:
                row = line.split(",")
                # keep tracking the different subReddits
                subReddits.add(row[2])
                if row[1] in userSR:
                    userSR[row[1]].add(row[2])
                else:
                    userSR[row[1]] = set()
                    userSR[row[1]].add(row[2])
    print 'Ended processing at: ' + str(time.ctime())

print 'Before dropping users with less than 2 SubReddit contributions, the unique count was: ' + str(len(userSR.keys()))

for key in userSR.keys():
    if len(userSR[key]) < 2:
        del userSR[key]
    else:
        userSR[key] = sorted(list(userSR[key]))

print 'After dropping users with less than 2 SubReddit contributions, the unique count was: ' + str(len(userSR.keys()))

print 'Ended record selection processing at: ' + str(time.ctime())

# store the user-subreddit dictionary to file...
with open('output\userSR.json', 'w') as fp_subReddit:
    json.dump(userSR, fp_subReddit)

# store list of all unique subreddits to file...
with open('output\subreddits.csv', 'w') as fp_data:
    writer = csv.writer(fp_data)
    writer.writerow(list(subReddits))
