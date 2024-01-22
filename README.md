# NBA data project #

## Introduction ##

  Data that we are working on is a part of a big dataset which You can find here: https://github.com/fivethirtyeight/data/tree/master/nba-elo

  For this project codecademy limited the data to just 5 teams and 11 columns.

## Data analyse ##
### Analyzing relationships between Quant and Categorical ###

  The data has been subsetted for two smaller datasets:
  +  nba_2010    - related to games in 2010 season
  +  nba_2014    - related to games in 2014 season
    
I  compared  two teams - Knicks and Nets.
Count mean points scored  in 2010 and 2014: 
+ Knicks 2010 mean - 102,11
+ Nets 2010 mean - 98,32
+ Knicks 2014 mean - 98,59
+ Nets 2014 mean - 98,14

+ Mean difference for these two teams in 2010 was equal to 9,73 points
+ Mean difference for these two teams in 2014 was equal to 0,45 points

Next I prepared two overlaping histograms to visualise distribution of scored points:

  ![season 2010 histplot](https://github.com/GrzegorzCiepiel/codecademy_NBA_project/assets/135313652/1d53373c-f9ff-4fc7-9a47-1fed0af51a31)
![season 2014 histplot](https://github.com/GrzegorzCiepiel/codecademy_NBA_project/assets/135313652/f4892cae-f088-48a1-aaf4-d7cd43744118)

 As we can see in 2010 Knicks did better. Their scored points spread is more on right side and it means that takes higher values.
 Knicks finished season at 11-th place and Nets finished at 15-th place ( the last one )

Last thing in this part was checking how all 5 teams from the dataset did in 2010?
I created side by side box plot with scored points at y-axis and teams at x-axis.

![Points scored by 5 teams in 2010](https://github.com/GrzegorzCiepiel/codecademy_NBA_project/assets/135313652/e01d8084-f968-4179-b658-14daa0deb890)

As we can see New Jersey Nets were the weakest team with the lowest average number of points scored but also the lowest minimum and maximum number of points scored.

### Analyzing relationships between Categorical variables ###

The question is - do teams tend to win more games at home compared to away?

I analysed colums: game_result (Win/Loose) and game_location (Home/Away) using pd.crosstab function.






 

 
