import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import chi2

#kai pali i logiki tou kwdika einai i idia me tous proigoumenous
#i diafora einai sto oti exoume mia for gia kanoume 1000 permutations
input_file = pd.read_csv('data_a4.csv',index_col = None)
#list of X values
X = input_file['X'].to_list()
#list of Y values
Y = input_file['Y'].to_list()
#a list containing all the t statistics
#t_stat[0] tha exei mesa to prwto t statistic prin ta permutations
t_stat = []


for i in range(1000):
    
    counter00 = 0;
    counter01 = 0;
    counter10 = 0;
    counter11 = 0;

    for k in range(1000):
        if(X[k] == 0 and Y[k] == 0):
            counter00 = counter00 + 1
        elif(X[k] == 0 and Y[k] == 1):
            counter01 = counter01 + 1
        elif(X[k]== 1 and Y[k] == 0):
            counter10 = counter10 + 1
        elif(X[k] == 1 and Y[k]==1):
            counter11 = counter11 + 1

    #we calculate the observed values and make it an array
    observed_values =  np.zeros((3,3))
    total = counter00 + counter10 + counter01 + counter11
    observed_values[0][0] = counter00 
    observed_values[0][1] = counter01 
    observed_values[1][0] = counter10 
    observed_values[1][1] = counter11 
    observed_values[0][2] = counter00 + counter01 
    observed_values[1][2] = counter10 + counter11 
    observed_values[2][0] = counter00 + counter10 
    observed_values[2][1] = counter01 + counter11 
    observed_values[2][2] = total 
    expected_values = np.zeros((2,2))

    #we calculate the expected values and we make an array to store them
    for m in range(2):
        for j in range(2):
            p1 = observed_values[m][2]/total
            p2 = observed_values[2][j]/total
            expected_values[m][j] = total*p1*p2

    #we calculate the t_statistic and we append it to the list
    t = 0
    for n in range(2):
        for j in range(2):
            nominator = (observed_values[n][j] - expected_values[n][j])
            nominator = nominator*nominator
            denominator = expected_values[n][j]
            t = t + nominator/denominator
            
    t_stat.append(t)
    
    #we shuffle the values of X
    random.shuffle(X)
  
#we start to calculate the p-value
first_stat = t_stat[0]
counter = 0
for i in range(1000):
    if(t_stat[i] >= first_stat and i != 0):
        counter = counter + 1
        
p_value = counter/1000 

#check if we accept or reject the null hypothesis
if(p_value < 0.05): 
    print("We reject H0 because p_value < 0.05") 
else:
    print("We accept H0 beacuse p_value > 0.05")
 

#let's start to plot the histogram of chi square statistics
#plot 1
plt.hist(t_stat, density=False, bins=30)  
plt.title('distribution of X^2 statistics from 1000 permutations')
plt.ylabel('occurances')
plt.xlabel('t-statistics')

#let's start to plot the other one
#plot 2
#bins = np.linspace(0, 10, 30)
#bin_centers = 0.5*(bins[1:] + bins[:-1])
#pdf = chi2.pdf(bin_centers,df = 1)
#plt.figure(figsize=(6, 4))
#plt.plot(bin_centers, pdf, label="PDF of df = 1")
#plt.ylabel('occurances')
#plt.xlabel('Chi square t-statistic')
#plt.title('distribution of X^2 statistics from 1000 permutations')
#plt.axvline(t_stat[0],color='r')
#plt.legend()

plt.show()