import pandas as pd
import random
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


def TrainRF(X, Y, n_trees, min_sample_leaf):
    clf = []
    t = min_sample_leaf
    for k in range(n_trees):    #posa dentra theloume na paragoume
        #arxikopoiei ta bootstrapped datasets 
        bootX = [[0] * 6] * len(X)  
        bootY = [[0] * 1] * len(X)
        for i in range(len(X)):   
            random_boot = random.randint(0, len(X)-1)
            bootX[i] = X[random_boot]   #to bootX[i] tha parei oli ti grammi tou X sth thesi random_boot
            bootY[i] = Y[random_boot]
        #molis ftasoume edw simainei oti exoume to bootstrapped dataset mas
        temp = tree.DecisionTreeClassifier(min_samples_leaf = t, max_features = "sqrt")
        #apothikeuse to apotelesma kai sinexise tin idia diadikasia
        clf.append(temp.fit(bootX, bootY))
    return clf
    

def PredictRF(model, X):
    predictions = []    #this list will contain all the predictions we will make
    for i in range(len(X)): #X[i] is the i'th row of X
        counter0 = 0
        counter1 = 0
        for m in range(len(model)): #m will be the number of trees
            #for each tree take the prediction of the X's row 
            k = model[m].predict([X[i]]) 
            #count how many 0 and 1 we have
            if(k == 0.0):
                counter0 = counter0 + 1
                
            elif(k == 1.0):
                counter1 = counter1 + 1
        
        #when you finish the trees make the prediction
        if(counter0 >= counter1):
            predictions.append(0)
            
        elif(counter0 < counter1):
            predictions.append(1)
    
    return predictions


df = pd.read_csv('Dataset6.1_XY.csv',index_col = None)
#take 70% of the whole dataset for training data
train_data = df.sample(frac = 0.7)
#take the rest 30% for testing data
test_data = df.drop(train_data.index)
X = train_data[['X1 transaction date', 'X2 house age','X3 distance to the nearest MRT station','X4 number of convenience stores','X5 latitude','X6 longitude']].to_numpy()
Y = train_data[['Y is house valuable']].to_numpy()
test = test_data[['X1 transaction date', 'X2 house age','X3 distance to the nearest MRT station','X4 number of convenience stores','X5 latitude','X6 longitude']].to_numpy()
exp = test_data[['Y is house valuable']].to_numpy()
res_model = []
predict_y = []
number_of_trees = 100
res_model = TrainRF(X,Y,number_of_trees,10)
predict_y = PredictRF(res_model, test )

#let's compair the result with the Random Forest Classifier

clf=RandomForestClassifier(n_estimators=number_of_trees,min_samples_leaf=1,max_features='sqrt')
clf.fit(X,Y.ravel())
y_pred=clf.predict(test)

count_diff = 0
for i in range(len(test)):
    if(predict_y[i]!=y_pred[i]):
        count_diff = count_diff + 1
p = 1 - (count_diff/len(test))
print("The probability our prediction is the same as random forest classifier is ",p,"%")

#we will use the test dataset to calculate the accuracy of the whole forest
correct = 0
wrong = 0
for i in range(len(test_data)):
    if(predict_y[i] == exp[i]):
        correct = correct + 1
accuracy_forest = correct/len(test_data)
print("Accuracy of forest is ",accuracy_forest)

#we will use the test dataset to calculate the accuracy of each of the 100 trees
acc = []
for i in range(number_of_trees):
    c1 = 0
    for j in range(len(test)):
        if(res_model[i].predict(test[[j]]) == exp[j]):
            c1 = c1 + 1
    acc.append(c1/len(test))
        
#histogram
plt.hist(acc, bins = 20)
plt.ylabel('occurances')
plt.xlabel('accuracy of trees')
plt.title('Accuracies')
plt.axvline(sum(acc)/len(acc),color='r',label = 'mean of accuracies trees')
plt.axvline(accuracy_forest,color = 'g',label = 'accuracy of whole forest')
plt.legend()
plt.show()   
        
