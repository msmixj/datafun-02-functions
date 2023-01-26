"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

#Statistic calculations for agility scores
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
variance = statistics.variance(scores)
stddev = statistics.stdev(scores)

#Use linear regression to calculate the slope and intercept of the best fit line.
slope,intercept = statistics.linear_regression(x_times,y_temps)

#Estimate the future temperature at the next hour.
#Choose a y-value off in future (y future)
y_future=13
x_future = round(slope * y_future + intercept)

print("-------------------------------------------------")
#This is where I will print the statistics functions.
print()
print(f"    mean={mean:.2f}")
print(f"    median={median:.2f}")
print(f"    mode={mode:.2f}")
print(f"    variance={variance:.2f}")
print(f"    stddev={variance:.2f}")
print(f"    slope={slope:.2f}")
print(f"    intercept={intercept:.2f}")
print()
print(f"    At y_future={y_future:d}")
print(f"    we predict the value of x will be {x_future:d}.")