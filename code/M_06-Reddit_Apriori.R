# Apriori on user-SubReddit data

# Author: Vivek M Agrawal (vagrawal39@gatech.edu)

# References:
# - https://cran.r-project.org/web/packages/arules/arules.pdf
# - https://cran.r-project.org/web/packages/arules/vignettes/arules.pdf
# - https://cran.r-project.org/web/packages/arulesViz/.../arulesViz.pdf
# - http://www.salemmarafi.com/code/market-basket-analysis-with-r/

# Load the libraries
library(arules);
library(arulesViz);
library(tictoc);

# set working directory
setwd("~/R/Apriori");

## --- UNCOMMENT FOR FIRST RUN

# Load the user-SubReddit data as Transaction class (specific to package arules)
# - input file format: comma delimeted
# - transaction format: 'basket' denoting each line is a separate transaction
# - rm.duplicates: FALSE
matchedSR = read.transactions(file='matchedSR', format="basket", rm.duplicates=FALSE, sep=",");

# save the transaction file to system for retrieval in case of script failure
save(matchedSR, file = 'matchedSR.rda');

## ---


## +++ LOAD STORED DATA IN CASE OF MEMORY FAILURE

# if failure, load previously saved transaction file from working directory
load('matchedSR.rda');

## +++ 


## <><> DIAGNOSTIC CODE

# plot SubReddit frequency plot for the top 20 items
itemFrequencyPlot(matchedSR, topN=20, type="absolute");

# list all subReddits picked by the Transaction dataset
itemInfo(matchedSR)

# summary of subReddits picked by the Transaction dataset
summary(matchedSR)

## <><> 

tic();

# Get the rules
rules <- apriori(matchedSR, parameter=list(supp=0.000004, conf=0.15, maxlen=10));
toc();

# save the rules file to csv
write(rules, file = "rules", sep=",", quote=TRUE);

# Show the top 5 rules
inspect(rules[1:5]);

# sort rules by confidence to have the most likely rules on top of the list
rules_sorted <- sort(rules, by=c("confidence", "support"), decreasing=TRUE);

# Show the top 5 rules - sorted
inspect(rules_sorted[1:5]);

# concise rules listing with only 3 constituents, using "maxlen" parameter
rules_concise <- apriori(matchedSR, parameter=list(supp=0.00005, conf=0.85, maxlen=4));

# Show the top 5 rules - concise
inspect(rules_sorted[1:5]);

# visualize the rules
plot(rules_concise, method="graph", interactive=TRUE, shading=T);

# check rules for specific lhs or rhs

# Pg. 75 of arules.pdf
# %in% - IN || %pin% - PARTIAL IN || %ain% - ALL IN

# check for keyword on RHS - uses %in%
rules_rhs <- subset(rules, subset = rhs %in% 'linux');

# sort rules by confidence to have the most likely rules on top of the list
rules_rhs <- sort(rules_rhs, by=c("confidence", "support", "lift"), decreasing=TRUE);

inspect(rules_rhs[1:5]);

# check for keyword on LHS - uses %pin%
rules_lhs <- subset(rules, subset = lhs %pin% 'nba');

# sort rules by confidence to have the most likely rules on top of the list
rules_lhs <- sort(rules_lhs, by="confidence", decreasing=TRUE);

inspect(rules_lhs[1:5]);

# plot the top 50 associations
rules_rhs_top <- head(rules_rhs, 50);
plot(rules_rhs_top, method="graph", interactive=TRUE, shading=T);

rules_lhs_top <- head(rules_lhs, 25);
plot(rules_lhs_top, method="graph", interactive=TRUE, shading=T);
