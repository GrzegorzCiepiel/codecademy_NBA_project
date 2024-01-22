import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head(5))
print('\n')
print(nba_2014.head(5))
print('\n')
print(nba.columns)

# Task 1
# The data has been subset for you into two smaller datasets:
# games from 2010 (named nba_2010) and games from 2014 (named nba_2014). To start, let’s focus on the 2010 data.
#
# Suppose you want to compare the knicks to the nets with respect to points earned per game. Using the pts column
# from the nba_2010 DataFrame, create two series named knicks_pts (fran_id = "Knicks") and nets_pts(fran_id = "Nets")
# that represent the points each team has scored in their games.

knicks_pts = nba_2010.pts[nba_2010.fran_id == "Knicks" ]
nets_pts = nba_2010.pts[nba_2010.fran_id == "Nets" ]
print(knicks_pts)
print(nets_pts)

# Task 2
# Calculate the difference between the two teams’ average points scored and save the result as diff_means_2010.
knicks_pts_mean = knicks_pts.mean()
nets_pts_mean = nets_pts.mean()
print(round(knicks_pts_mean, 2))
print(round(nets_pts_mean, 2))
diff_means_2010 = abs(round(knicks_pts_mean - nets_pts_mean,2))
print(diff_means_2010)

# Task 3
# Rather than comparing means, it’s useful look at the full distribution of values to understand whether a difference
# in means is meaningful. Create a set of overlapping histograms that can be used to compare the points scored for
# the Knicks compared to the Nets. Use the series you created in the previous step (1) and the code below to create
# the plot. Do the distributions appear to be the same?

plt.hist(knicks_pts, alpha=.8, density=True, label='Knicks')
plt.hist(nets_pts, alpha=.8, density=True, label='Nets')
plt.legend()
plt.title("2010 Season")
plt.show()

print('Knicks points distribution looks weird ')

# Task 4
# Now, let’s compare the 2010 games to 2014. Replicate the steps from Tasks 2 and 3 using nba_2014. First, calculate
# the mean difference between the two teams points scored. Save and print the value as diff_means_2014. Did the
# difference in points get larger or smaller in 2014? Then, plot the overlapping histograms. Does the mean difference
# you calculated make sense?

knicks_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Knicks" ]
nets_pts_2014 = nba_2014.pts[nba_2014.fran_id == "Nets" ]
print(knicks_pts_2014)
print(nets_pts_2014)
knicks_pts_14_mean = knicks_pts_2014.mean()
nets_pts_14_mean = nets_pts_2014.mean()
print(round(knicks_pts_14_mean, 2))
print(round(nets_pts_14_mean, 2))
diff_means_2014 = abs(round(knicks_pts_14_mean - nets_pts_14_mean,2))
print(diff_means_2014)

plt.hist(knicks_pts_2014, alpha=.8, density=True, label='Knicks')
plt.hist(nets_pts_2014, alpha=.8, density=True, label='Nets')
plt.legend()
plt.title("2014 Season")
plt.show()
plt.clf()

# Task 5
# For the remainder of this project, we’ll focus on data from 2010. Let’s now include all teams in the dataset
# and investigate the relationship between franchise and points scored per game.
# Using nba_2010, generate side-by-side boxplots with points scored (pts) on the y-axis and team (fran_id) on the
# x-axis. Is there any overlap between the boxes? Does this chart suggest that fran_id and pts are associated?
# Which pairs of teams, if any, earn different average scores per game?

sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.show()
plt.clf()

# Task 6
# We'd like to know if teams tend to win more games at home compared to away.
#
# The variable, game_result, indicates whether a team won a particular game ('W' stands for “win” and 'L' stands for
# “loss”). The variable, game_location, indicates whether a team was playing at home or away ('H' stands for “home”
# and 'A' stands for “away”).
#  Calculate a table of frequencies that shows the counts of game_result and game_location.
# Save your result as location_result_freq and print your result. Based on this table, do you think the variables
# are associated?`


location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

# Task 7
# Convert this table of frequencies to a table of proportions and save the result as location_result_proportions.
location_result_proportions = pd.crosstab(nba_2010.game_result, nba_2010.game_location, normalize=True)
print(location_result_proportions )

# Task 8
# Using the contingency table created above (Task 6), calculate the expected contingency table (if there were no
# association) and the Chi-Square statistic.

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)
# Does the actual contingency table look similar to the expected table — or different? Based on this output, do you
# think there is an association between these variables?
#
print('For a 2x2 table, Chi-squared greater than about 4 indicates an association. Result is equal to 6.5 so surly '
      'there is association between location and a score.' )

# Task 9
# For each game, 538 has calculated the probability that each team will win the game. We want to know if teams with
# a higher probability of winning (according to 538) also tend to win games by more points.
# In the data, 538's prediction is saved as forecast. The point_diff column gives the margin of victory/defeat for
# each team (positive values mean that the team won; negative values mean that they lost).
# Using nba_2010, calculate the covariance between forecast (538's projected win probability) and point_diff (the
# margin of victory/defeat) in the dataset. Save and print your result. Looking at the matrix, what is the covariance between these two variables?

cov_forecast_pointdiff = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(cov_forecast_pointdiff)
print('Covariance between probability that ech team will win the game and the margin of victory/defeat is equal to 1.37 \n'
      ' and that says there is no relationship between these two values ')
# Task 10
# Because 538’s forecast variable is reported as a probability (not a binary), we can calculate the strength of
# the correlation.
#
# Using nba_2010, calculate the correlation between forecast and point_diff. Call this point_diff_forecast_corr.
# Save and print your result. Does this value suggest an association between the two variables?

point_diff_forecast_corr, p = pearsonr(x=nba_2010.forecast, y=nba_2010.point_diff)
print(point_diff_forecast_corr)
print('Pearsonr correlation between probability that ech team will win the game and the margin of victory/defeat \n'
      'is equal to 0.45. This means that there is correlation between this two variables. ' )
# Task 11
# Generate a scatter plot of forecast (on the x-axis) and point_diff (on the y-axis). Does the correlation value
# make sense?

plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()
plt.clf()

print('Scatter plot between forecast and point_diff columns confirms positive correlation between them')