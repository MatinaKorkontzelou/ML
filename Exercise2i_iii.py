#Edw ulopoiountai oi askiseis Exercise 2 i kai iii

import matplotlib.pyplot as plt
import numpy as np

def Bayes_function(probability_photon):
    probability_non_photon = 1 - probability_photon
    numerator = 0.85*probability_photon
    denominator = numerator + 0.1*probability_non_photon
    result = numerator/denominator
    return result

#i)

photon = 1e-7 

photon_when_reported = Bayes_function(photon)
print("The probability that a photon package was actually received is ")
print(photon_when_reported)

#iii)

temp = np.random.normal(1e-7,9e-8,size = 10000) #sample from N(μ,σ) 10.000 values
sampling = []   #it will have only the positive values
for i in range(10000):
    if temp[i] >= 0:
       sampling.append(temp[i])

probability_of_package_reception = []
for j in range(len(sampling)):
   probability_of_package_reception.append(Bayes_function(sampling[j]))
  
plt.title("Distribution of probability of package reception")
plt.xlabel("S : possibility of package reception")
plt.ylabel("occurances of S")
plt.hist(probability_of_package_reception)
plt.show()