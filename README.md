# Reddit Recommender in R

Applies Apriori Algorithm to recommend sub-reddits to users based on their commenting history on specific topics. 

Hypothesis based on the reasoning that users with similar tastes will visit similar subreddits and statistically more likely to comment on similar topics.

Apriori essentially is:
> ...an algorithm for frequent item set mining and association rule learning over transactional databases. The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends in the database: this has applications in domains such as market basket analysis.

[Source: Wikipedia](https://en.wikipedia.org/wiki/Apriori_algorithm)

Challenge is to convert reddit comments to Market basket equivalent. Implementation approach is to treat comment ‘author’ as Purchase Identifier and ‘subreddit’ as Items to test the stated hypothesis.

Implementation in R using [aRules package](https://cran.r-project.org/web/packages/arules/index.html).

## Dataset Description

Analysis based on [2015 Reddit Comments Corpus](https://archive.org/details/2015_reddit_comments_corpus)

* Source:reddit.com (hosted on archive.org)
* Volume: 1.65 billion comments from 2007 to May 2015
* Size: ~5 GB Monthly (Compressed), ~30 GB Monthly (Uncompressed)
* Format: JSON
* Granularity: Individual comment level
* Target Data: May 2015 slice

## Sample JSON Object
```json
{"gilded":0,"author_flair_text":"Male","author_flair_css_class":"male","
retrieved_on":1425124228,"ups":3, "subreddit_id":"t5_2s30g" ,"edited":false,"
controversiality":0, "parent_id":"t1_cnapn0k" ,"subreddit":"AskMen" ,"body":"I
can't agree with passing the blame, but I'm glad to hear it's at least
helping you with the anxiety. I went the other direction and started taking
responsibility for everything. I had to realize that people make mistakes
including myself and it's gonna be alright. I don't have to be shackled to
my mistakes and I don't have to be afraid of making them. ","created_utc":"
1420070668","downs":0, "score":3,"author":"TheDukeofEtown" ,"archived":false,"
distinguished":null, "id":"cnasd6x" ,"score_hidden":false, "name":"
t1_cnasd6x" ,"link_id":"t3_2qyhmp"}
```

# Implementation






# Results


