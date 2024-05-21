import pandas as pd
import numpy as np
from scipy.stats import chi2



input_file = pd.read_csv('data_a4.csv',index_col = None)

counter00 = 0;
counter01 = 0;
counter10 = 0;
counter11 = 0;

#ta X,Y tha einai listes opou to kathe ena tha exei tis times twn X,Y antistoixa
X = input_file['X'].to_list()
Y = input_file['Y'].to_list()
 
#counter00 antistoixei se X kai Y = 0. Metrame poses fores prokiptoun gia diafores times
#twn sindiasmwn tou X kai Y
for i in range(1000):
    if(X[i] == 0 and Y[i] == 0):
        counter00 = counter00 + 1
    elif(X[i] == 0 and Y[i] == 1):
        counter01 = counter01 + 1
    elif(X[i]== 1 and Y[i] == 0):
        counter10 = counter10 + 1
    elif(X[i] == 1 and Y[i]==1):
        counter11 = counter11 + 1

#upologizoume ton observed_values table
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

#upologizoume ton expected_values table
for i in range(2):
    for j in range(2):
        p1 = observed_values[i][2]/total
        p2 = observed_values[2][j]/total
        expected_values[i][j] = total*p1*p2
 
#t einai to chi square statistic
t = 0
for i in range(2):
    for j in range(2):
        nominator = (observed_values[i][j] - expected_values[i][j])
        nominator = nominator*nominator
        denominator = expected_values[i][j]
        t = t + nominator/denominator

#calculate p_value
print("T_stat : ",t)
p_value = 1 - chi2.cdf(t , df=1)
print("To p_value exei timi : ",p_value)
if(p_value < 0.05):
    print("Aporriptoume tin Ho")
else:
    print("Dexomaste tin Ho")