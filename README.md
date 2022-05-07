Computational Argumentation 2022 -- Assignment 1
================================================

This file describes the expected usage of the main Python file and description of the statistics.


## Python file
The main.py file contains our source code.
The file has several functions and all the functions are called in the main method. 
The program does following tasks - 
1. Read csv file present in "data" folder.
2. Transforming data 
3. Extracting only arguementative records from the data.
4. Splitting data into Train, Test and Validate sets in 70:20:10 ratio respectively.
5. Writing the combined arguements and splitted data into CombinedArguements.json, Train.json, Test.json, Validate.json respectively.
6. Computing and plotting statistics(Description of statistics below)

## Statistics Description

The statistics are computed taking non-arguementative records into account.

1. Corelation between argument_quality_score and effectiveness_score -
We took mean of arguement_quality_score and effectiveness_score, and plotted a scatter plot between them. 
We found out that there is a strong co-relation between them(co-relation score - 0.89). We can say thar if the arguement quality is high we can assume that effectiveness score is also high and vice-versa.

2. Histogram plotted for number of arguementative and non-arguementative annotations per issue - 
We are interested to look at how many records are marked arguementative or non-arguementative per issue by the annotators.
We observe that the number of non-arguementative records are pretty less as compared to the number of arguementative records and thus we have more data per issue to calculate the effectiveness and quality score.

