import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2

input_file = pd.read_csv('data_a4.csv',index_col = None)
#i logiki tou kwdika einai i idia me tou C.py
#apla ta grafoume dio fores gia tous dio pinakes
#enas pinakas gia Z = 0 kai enas gia Z = 1
X = input_file['X'].to_list()
Y = input_file['Y'].to_list()
Z = input_file['Z'].to_list() 

observed_values1 =  np.zeros((3,3)) #for Z=0
observed_values2 =  np.zeros((3,3)) #for Z=1

counter00 = 0;
counter01 = 0;
counter10 = 0;
counter11 = 0;

#upologizoume ta observed_values gia Z = 0
for i in range(1000):
    if(Z[i] == 0):
        if(X[i] == 0 and Y[i] == 0):
            counter00 = counter00 + 1
        elif(X[i] == 0 and Y[i] == 1):
            counter01 = counter01 + 1
        elif(X[i]== 1 and Y[i] == 0):
            counter10 = counter10 + 1
        elif(X[i] == 1 and Y[i]==1):
            counter11 = counter11 + 1
            
observed_values =  np.zeros((3,3))
total1 = counter00 + counter10 + counter01 + counter11
observed_values1[0][0] = counter00 
observed_values1[0][1] = counter01 
observed_values1[1][0] = counter10 
observed_values1[1][1] = counter11 
observed_values1[0][2] = counter00 + counter01 
observed_values1[1][2] = counter10 + counter11 
observed_values1[2][0] = counter00 + counter10 
observed_values1[2][1] = counter01 + counter11 
observed_values1[2][2] = total1 

counter00 = 0;
counter01 = 0;
counter10 = 0;
counter11 = 0;

#upologizoume ta observed_values gia Z = 1
for i in range(1000):
    if(Z[i] == 1):
        if(X[i] == 0 and Y[i] == 0):
            counter00 = counter00 + 1
        elif(X[i] == 0 and Y[i] == 1):
            counter01 = counter01 + 1
        elif(X[i]== 1 and Y[i] == 0):
            counter10 = counter10 + 1
        elif(X[i] == 1 and Y[i]==1):
            counter11 = counter11 + 1
            
observed_values2 =  np.zeros((3,3))
total2 = counter00 + counter10 + counter01 + counter11
observed_values2[0][0] = counter00 
observed_values2[0][1] = counter01 
observed_values2[1][0] = counter10 
observed_values2[1][1] = counter11 
observed_values2[0][2] = counter00 + counter01 
observed_values2[1][2] = counter10 + counter11 
observed_values2[2][0] = counter00 + counter10 
observed_values2[2][1] = counter01 + counter11 
observed_values2[2][2] = total2


expected_values1 = np.zeros((2,2))

#calculate the expected_values table for Z = 0
for i in range(2):
    for j in range(2):
        p1 = observed_values1[i][2]/total1
        p2 = observed_values1[2][j]/total1
        expected_values1[i][j] = total1*p1*p2
        
expected_values2 = np.zeros((2,2))

#calculate the expected_values table for Z = 1
for i in range(2):
    for j in range(2):
        p1 = observed_values2[i][2]/total2
        p2 = observed_values2[2][j]/total2
        expected_values2[i][j] = total2*p1*p2
        
        
#t1 is the X^2 for Z = 0
t1 = 0
for i in range(2):
    for j in range(2):
        nominator = (observed_values1[i][j] - expected_values1[i][j])
        nominator = nominator*nominator
        denominator = expected_values1[i][j]
        t1 = t1 + nominator/denominator

#t2 is the X^2 for Z = 1
t2 = 0
for i in range(2):
    for j in range(2):
        nominator = (observed_values2[i][j] - expected_values2[i][j])
        nominator = nominator*nominator
        denominator = expected_values2[i][j]
        t2 = t2 + nominator/denominator
        
#calculate p_value1
p_value1 = 1 - chi2.cdf(t1 , df=1)

#calculate p_value2
p_value2 = 1 - chi2.cdf(t2 , df=1)
p_value = p_value1 + p_value2

print("T_stat1 : ",t1," T_stat2 : ",t2)
print("To p_value otan Z = 0 einai ",p_value1)
print("To p_value otan Z = 1 einai",p_value2)
print("To athroisma tous einai",p_value)

if(p_value1 < 0.05 and p_value2 < 0.05 and p_value < 0.05):
    print("Aporriptoume to Ho")
else:
    print("Apodexomaste to Ho")