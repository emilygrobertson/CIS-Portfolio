# CIS 443-01
# Program 2
# Due: Monday October 12th, 2020
# Grading ID: D7759
# Description: This program aims to show the minimum, maximum, 
# range, mean, median, mode, variance and standard deviation for a certain list of Cafeteria Food ratings.

import statistics as stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5] #list of student responses
array = np.array(responses)
print("Minimum = " +str(np.amin(array))) #Printing the Minimum
print("Maximum = " +str(np.amax(array))) #Printing the Maximum
print("Range = " +str(np.ptp(array))) #Printing the Range
print("Mean = " +str(stats.mean(array))) #Printing the Mean
print("Median = " +str(stats.median(array))) #Printing the Median
print("Mode = " +str(stats.mode(array))) #Printing the Mode
print("Variance = " +str(stats.pvariance(array))) #Printing the Variance
print("Standard Deviation = " +str(stats.pstdev(array))) #Printing the Standard Deviation

values= [1,2,3,4,5]
values, frequencies= np.unique(array, return_counts=True)

title = f'Quality of Food at JCPS Cafeteria' # this will display the title for the Graph
sns.set_style('whitegrid')
axes = sns.barplot(x= values, y = frequencies, palette='bright') #Defines X & Y axes

axes.set_title(title)
axes.set(xlabel='Rating: 1 = Awful & 5 = Excellent', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) *1.10)

for bar, frequency in zip(axes.patches, frequencies): #For Loop to display the dimensions of the Bar Graph
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(array):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')


plt.show()
