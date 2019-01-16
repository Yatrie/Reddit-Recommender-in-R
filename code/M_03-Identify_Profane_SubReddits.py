'''
Module to identify obscene / objectionable SubReddits from the Reddit comments data

Uses hand-curated bad-words list derived based on lists at following sources:
http://contentfilter.futuragts.com/phraselists/
https://raw.githubusercontent.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en

@author: Vivek M Agrawal (vagrawal39@gatech.edu)

Requires Python 2.7
'''

profane_subReddits = set()

with open('output\subreddits.csv', 'r') as data_file:
    for line in data_file:
        subReddits = sorted(line.split(","))

print 'Count of SubReddits before Obscenity Filtering: ' + str(len(subReddits))

with open('bad-words.txt', 'rb') as data_file:
    badWords = data_file.read().splitlines()
    
print 'Count of words in Obscenity Filter: ' + str(len(badWords))

for sR in subReddits:
    for bW in badWords:
        if bW.lower() in sR.lower():
            profane_subReddits.add(sR)
        
print 'Count of objectionable SubReddits identified after Obscenity Filtering: ' + str(len(profane_subReddits))

with open('output\profane_subReddits', 'w') as fp:
    for item in profane_subReddits:
      fp.write("%s," % item)
