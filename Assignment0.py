import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

#Task 1.1

#1.
casts = pd.read_csv('heart.csv',index_col = None)
#I printed them just to be sure
print(casts.head())     
print(casts.tail())

#2.
min = casts.to_numpy().min(axis=None)
print(min)

#3.
mean = casts.to_numpy().mean(axis = 0) #calculate the mean of every col
myDict = {} #this is the dictionary
i = 0 
for col in casts.columns:
    myDict[col] = mean[i]
    i = i + 1
    
#print(myDict)

maxKey = max(myDict, key = myDict.get)
print(maxKey) #here we can see that chol has the highest mean

#4.

cont_features_std_ascend = [] #i store the standard deviation of each column in a list

myD = {}
for i in range(0,13):
   if len(((casts.loc[:,casts.columns[i]].unique()))) >= 10: #we check if the unique values are over or equal to 10
       cont_features_std_ascend.append(st.stdev(casts.loc[:,casts.columns[i]])) #if they are , we append them to the list
           
cont_features_std_ascend.sort() #sort in asceding order
names_of_features = ['olapeak','age','trestbps','thalack','chol'] #sorted just like their values

#5.
#shuffle the casts dataframe and take the 70% percent of that
dataframe1 = casts.sample(frac = 0.7, random_state = 200)
#print(dataframe1)
#take the rest 30% percent of casts dataframe
dataframe2 = casts.drop(dataframe1.index)
#print(dataframe2)


#6.
data1 = dataframe1[dataframe1['hasHeartDisease'] > 0].copy()
#print(data1)
data2 = dataframe2[dataframe2['hasHeartDisease'] > 0].copy()
#print(data2)

data1.to_csv('dataframe1.csv',index = False)
data2.to_csv('dataframe2.csv',index = False)

#Task 1.2

#1.
def my_plot_func(feature1, feature2 = None , action = 'scatter-plot'):
    if(action == 'scatter-plot'):
        x = feature1.to_numpy()
        y = feature2.to_numpy()
        x = np.array(x)
        y = np.array(y)
        plt.scatter(x,y)
        plt.xlabel(feature1.name)
        plt.ylabel(feature2.name)
        plt.show()
    elif(action == 'histogram'):
        plt.hist(feature1, 10)
        plt.xlabel(feature1.name)
        plt.ylabel('how frequently the values on the x-axis occur in the data')
        plt.show()
    elif(action == 'line'):
        xpoints = np.array(feature1)
        ypoints = np.array(feature2)
        plt.xlabel('names')
        plt.ylabel('standard deviation')
        plt.plot(xpoints,ypoints)
        plt.show()
    else:
        print('Wrong Action')
        return
        
       
#2.
casts = pd.read_csv('heart.csv',index_col = None)
my_plot_func(casts.age,casts.hasHeartDisease)

#3.
F1 = (casts.trestbps - casts.chol).abs() #i toke the asbolute value , beacause i didn't
                                         #want to have negatives
F2 = pow(casts.age,casts.sex) + 1
df1 = pd.DataFrame(F1)
df2 = pd.DataFrame(F2)
df1_new = df1.rename(columns={0: 'trestbpsMinusChol'})
df2_new = df2.rename(columns={0: "agePowSexPlusOne"})
my_plot_func(df1_new.trestbpsMinusChol,df2_new.agePowSexPlusOne)

#4.
mean1 = df1_new.trestbpsMinusChol.to_numpy().mean(axis = None)
mean2 = df2_new.agePowSexPlusOne.to_numpy().mean(axis = None)
if(mean1 > mean2):
   my_plot_func(df1_new.trestbpsMinusChol,action='histogram')
else:
    my_plot_func(df2_new.agePowSexPlusOne,action='histogram')        


#5.
x = names_of_features
y = cont_features_std_ascend
my_plot_func(x,y,'line')

