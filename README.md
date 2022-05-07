Computational Argumentation 2022 -- Assignment 1
================================================

This file describes the expected usage of the main Python file and description of the statistics.


## main.py file
The main.py file contains our source code.
The file has several functions and all the functions are called in the main method. 
The program does following tasks - 
1. Read csv file present in "data" folder.
2. Transforming data 
3. Extracting only argumentative records from the data.
4. Splitting data into Train, Test and Validate sets in 70:20:10 ratio respectively.
5. Writing the combined arguments and split the data into CombinedArguements.json, Train.json, Test.json, Validate.json respectively.
6. Computing and plotting statistics(Description of statistics below)

## Statistics Description

The statistics are computed taking non-argumentative records into account.

1. Correlation between argument_quality_score and effectiveness_score -
We took mean of argument_quality_score and effectiveness_score, and plotted a scatter plot between them. 
We found out that there is a strong correlation between them(co-relation score - 0.89). We can say thar if the argument quality is high we can assume that effectiveness score is also high and vice-versa.

2. Histogram plotted for number of argumentative and non-argumentative annotations per issue - 
We are interested to look at how many records are marked argumentative or non-argumentative per issue by the annotators.
We observe that the number of non-argumentative records are pretty less as compared to the number of argumentative records and thus we have more data per issue to calculate the effectiveness and quality score.

