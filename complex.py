import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt
import math
m=5
wi=[7,8,8,6,9]
wivi2=[1,2,3,4,2]
B=[1.5,1.5,1.5,1.5,1.5]
W=200
C=175
V=110
alpha=[2.330,1.450,0.541,8.050,1.950]
new_population=[]
max_fitness=0
maxf=[]
meanf=[]
def newchorom():
    population=[]
    for i in range(100):
        sigma1=np.random.uniform(-1,1,5)
        sigma2=np.random.uniform(-0.01,0.01,5)
        ri=np.random.uniform(0,1,5)
        ni= np.random.randint(1,6,5)
        xi=np.hstack((ni,ri,sigma1,sigma2))
        xi=list(xi)
        population.append(xi)
    return population

def fitness(xi):
    n=xi[ :5]
    r=xi[5:10]
    R=[]
    fitness_value=0
    g1=0
    g2=0
    g3=0
    for i in range(5):
        R.append(1-((1-r[i])**n[i]))
          
    for i in range(5):
        g1+= wivi2[i]*(n[i]**2)
        g2+= ((alpha[i]/100000)*((-1000/np.log(r[i]))**B[i]))*(n[i]+np.exp(0.25*n[i]))
        g3+= (wi[i]*n[i])*(np.exp(0.25*n[i]))
 
    if g1-V > 0:
        fitness_value=0
    elif g2-C > 0:
        fitness_value=0
    elif g3-W > 0:
        fitness_value=0
    else:   
        fitness_value=R[0]*R[1]+R[2]*R[3]+R[0]*R[3]*R[4]+R[1]*R[2]*R[4]-R[0]*R[1]*R[2]*R[3]-R[0]*R[1]*R[2]*R[4]-R[0]*R[1]*R[3]*R[4]-R[0]*R[2]*R[3]*R[4]-R[1]*R[2]*R[3]*R[4]+2*R[0]*R[1]*R[2]*R[3]*R[4]
    
    return fitness_value

def parentselect(population):
    childern=[]
    for i in range(700):
        k=np.random.randint(0,100,2)
        child=recombination(population[k[0]],population[k[1]])
        childern.append(child)
    return childern

def recombination(parent1,parent2):
    miu=[]
    for i in range(20):
        miu.append((parent1[i]+parent2[i])/2)
    return miu  

  
def mutation(sigma,xi):
    Ni=np.random.normal(0,1,10)
    new_sigma=[]
    x=[]
    f=m+m
    t=1/((2*f)**0.5)
    t_=1/((2*(f**0.5))**0.5)
    #update sigma vs shartash
    for i in range(f):
        new_sigma.append(sigma[i]*(np.exp((t_*np.random.randn())+(t*Ni[i]))))
    for i in range(10):
        if new_sigma[i]<=0.001:
            new_sigma.remove(new_sigma[i])
            new_sigma.insert(i,0.001)
    #update n vs shartash       
    for i in range(m):
        x.append(np.round(xi[i]+(new_sigma[i]*Ni[i])))
    for i in range(m):
        if x[i]<= 1:
            x.remove(x[i])
            x.insert(i,1)
    #update r vs shartash 0 < r < 1       
    for i in range(5,10):
        x.append(xi[i]+(new_sigma[i]*Ni[i]))
    for i in range(5,10):
        if x[i]>=1:
            x.remove(x[i])
            x.insert(i,0.99)
        elif x[i]<= 0:
            x.remove(x[i])
            x.insert(i,0.01)
            
    x.extend(new_sigma)
    return x

def elitism_select(mutate_list):
    fitness_list=[]
    new_pop=[]
    max_fitness=0
    mean_fitness=0
    for i in mutate_list:
        fitness_list.append(fitness(i))
    z=sorted(zip(fitness_list,mutate_list))
    z.reverse()
    for i in range(100):
        new_pop.append(z[i][1])
    max_fitness=fitness(new_pop[0])
    fitness_list.sort()
    fitness_list.reverse()
    mean_fitness=np.mean(fitness_list[ :100])
    #print('max_fitness',max_fitness)
    return(new_pop,max_fitness,new_pop[0],mean_fitness)
    
            
population=newchorom()
for i in range(100):
    #print('iteration=',i)
    childern=parentselect(population)
    mutate_list=[]
    for i in childern:
        X=mutation(i[10: ],i[ :10])
        mutate_list.append(X)
    new_population,max_fitness,solution,mean_fitness=elitism_select(mutate_list)
    maxf.append(max_fitness)
    meanf.append(mean_fitness)
    if max_fitness==1:
        print('solution is',solution)
        break
    population=new_population   
print('solution is',solution)
print()
print('the best n for each subsystem is',solution[ :5])
print('the best r for each subsystem is',solution[5:10])
print('max of fitness in last generation is',maxf[99])
print()
print('six max fitness in six last generation=',maxf[94:100])
plt.style.use('seaborn')
plt.plot(maxf, color='blue',label='max fitness')
plt.legend()
plt.show()
plt.plot(meanf, color='red',label='mean fitness')
plt.legend()
plt.show()


        
























        


