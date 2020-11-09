# MSBA 443-01
# Fall 2020
# Program 2
# Solution by Andrew L. Wright

import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, counts = np.unique(responses, return_counts=True)

values = list(values)
counts = list(counts)

print('Reponses and frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')
    
# Text solution runs statistics on the counts not the values
# presumably because they are ordinal values
print('\nStatistics about counts - Text Solution')
print(f'Min response count: {values[counts.index(min(counts))]} occurred {min(counts)} time(s)')
print(f'Max response count: {values[counts.index(max(counts))]} occurred {max(counts)} time(s)')
print(f'Range of response counts: {min(counts)}-{max(counts)}')
print(f'Mean response count: {stats.mean(counts)}')
print(f'Median response count: {stats.median(counts)}')
print(f'Mode response count: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')

# Statistics about the values
# Doing this with ordinal values is controversial
# See: https://measuringu.com/mean-ordinal/
print('\nStatistics about (ordinal) values')
print(f'Min response value: {min(responses)}')
print(f'Max response value: {max(responses)}')
print(f'Range of response values: {min(responses)}-{max(responses)}')
print(f'Mean response value: {stats.mean(responses)}')
print(f'Median response value: {stats.median(responses)}')
print(f'Mode response value: {stats.mode(responses)}')
print(f'Population Variance: {stats.pvariance(responses)}')
print(f'Population Standard deviation: {stats.pstdev(responses)}')
print(f'Sample Variance: {stats.variance(responses)}')
print(f'Sample Standard deviation: {stats.stdev(responses)}')
    
sns.set_style('whitegrid')  # white backround with gray grid lines
axes = sns.barplot(values, counts, palette='bright')  # create bars
axes.set_title('Survey responses')  # set graph title
axes.set(xlabel='Response', ylabel='Frequency')  # label the axes

# scale y-axis by 10% to make room for text above bars
axes.set_ylim(top=max(counts) * 1.10)

# display frequency & percentage above each patch (bar)
for bar, count in zip(axes.patches, counts):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{count:,}\n{count / sum(counts):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')

plt.show()
