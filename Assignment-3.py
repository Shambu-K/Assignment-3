import math
import random
from scipy.stats import binom
import array as arr
import numpy as np

#Program to compare the simulated and theoretical result for type-1 and type-2 errors, for a given hypothesis
    
#Theoretical

#Type-1 Error- Rejecting null hypothesis(H_0) when it is true
p=2/3

#parameter 'n'
n=3

#possible values of random variable
vals=np.arange(0,4)


binom_val1=[binom.pmf(r,n,p) for r in vals]

#given that H_0 is rejected when X≥2
theo_res1=binom_val1[2]+binom_val1[3]
print("Theoretical Result: ")
print("Type-1 error - ",theo_res1)

#Type-2 Error- Not accepting alternate hypothesis(H_1) when it is true
q=1/3
binom_val1=[binom.pmf(r,n,q) for r in vals]

#Since alternate hypothesis H_1 is not accepted when X≤1
theo_res2=binom_val1[0]+binom_val1[1]
print("Type-2 error - ",theo_res2)


#Simulations

simlen = 1000000

q1 = 2/3
q2 = 1/3

#Performing simulations for Type-1 and Type-2 errors respectively
data_binom1 = binom.rvs(n,q1,size=simlen)
err_ind1 = np.nonzero(data_binom1>=2)
data_binom2 = binom.rvs(n,q2,size=simlen)
err_ind2 = np.nonzero(data_binom2<=1)

sim_res1 = np.size(err_ind1)/simlen
sim_res2 = np.size(err_ind2)/simlen
print("\nSimulated Result: ")
print("Type-1 error - ",sim_res1)
print("Type-2 error - ",sim_res2)

dif_1=abs(sim_res1-theo_res1)
dif_2=abs(sim_res2-theo_res2)
print("\nDifference between theoretical result and simulated result: ")
print("Type-1 error - ",dif_1)
print("Type-2 error - ",dif_2)



