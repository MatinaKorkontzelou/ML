import random
import matplotlib.pyplot as plt


#ii)

final_list = []         #final_list will contain the sum of each package(2000 in total)
for i in range(2000):
    photon_package = [random.randrange(10,50,10) for i in range(100)]
    final_list.insert(i,sum(photon_package)) 


plt.title("Distribution of total energies")
plt.xlabel("S : summed energies of each photon package")
plt.ylabel("p(S)")
plt.hist(final_list, density = True)
plt.show()





