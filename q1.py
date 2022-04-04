import copy
from random import randint
import random
import time
import csv


def individual(length, min, max):
    return [randint(min,max) for x in range(length)]

def individualMutate(min, max):
    return randint(min,max)

def fitness(plan):
    maxLimit = 7000
    duration = 5
    # foodbudget consist of 3 meals per day
    # total = hotelStar * duration + tourSpot * tourBudget + foodBudget * 3 * duration + transBudget * transFreq * 5
    total = plan[0] * duration + plan[1] * plan[2] + plan[3] * 3 * duration + plan[4] * plan[5] * duration
    #in this case fitness the lower the better , fitness is calculated using absolute value of maxLimit - total of current combinations
    fitness = abs(maxLimit - total)
    return fitness

def populate(num,vacPlan):
    totalFitness = 0
    hotelStar   = individual(num,200,300)
    tourSpot    = individual(num,2,13)
    tourBudget  = individual(num,200,400)
    foodBudget  = individual(num,20,30)
    transBudget = individual(num,40,65)
    transFreq   = individual(num,3,8)
    fitnessValue     = [0]*num
    newvacPlan = list(list(x) for x in zip( hotelStar , tourSpot , tourBudget , foodBudget , transBudget, transFreq, fitnessValue))
    for x in range(len(newvacPlan)):
        vacPlan.append(newvacPlan[x])
    for x in range(0,len(vacPlan)):
        vacPlan[x][6]=fitness(vacPlan[x])
        totalFitness+=vacPlan[x][6]
    #we sort the list according to the fitness value in ascending order
    vacPlan = sorted(vacPlan,key=lambda x:x[6])
    return vacPlan,totalFitness

def mutate(choice,list):
    match choice:
        case 0:
            list[0]=individualMutate(50,300)
            
        case 1:
            list[1]=individualMutate(2,13)
            
        case 2:
            list[2]=individualMutate(200,400)
            
        case 3:
            list[3]=individualMutate(10,30)
            
        case 4:
            list[4]=individualMutate(30,65)
            
        case 5:
            list[5]=individualMutate(3,8)
            
    
    return list

def tournamentSelect(vacPlan):
    random.shuffle(vacPlan)
    contestant = []
    for x in range(3):
        contestant.append(vacPlan[x]) 
    winner = min(contestant,key=lambda x:x[6])
    return winner

"""
Money on-hand | RM 7000
Vacation duration | 5 days
Hotel star rating | <RM300 per night
Tourist spots | 13 spots
One tourist spot | <RM400
Food price | <RM30 per meal - 3 meal per day so total 30*3*5
Transportation fees | <RM65 per trip 
Transport frequency | 8 trip per day - total 65*8*5
Max total = RM 9750
maintain population of 100 every generations
"""
maxLimit=7000
vacPlan =[]
data=[]
overallFitness=[]
gen1VacPlan, totalFitness= populate(100,vacPlan)
overallFitness.append(['gen1',totalFitness/100])
# we filter element that have fitness < 0 and repopulate to maintain 100 population, 
# later when selection > crossover > mutation do the same
for x in range(5):
    """
    below is selection by pairing (select pair from top best fitting)
    do selection > crossover > mutation for pairs each time
    """
    
    totalTimeRan=x
    start_time = time.time()
    looptime=0
    bestSolution =[]
    bestFound = True
    vacPlan= copy.deepcopy(gen1VacPlan)
    while bestFound:
        totalFitness=0
        newGeneration = []
        #0-99 in index crossover and mutate
        for x in range(2,100,2):
            father = vacPlan[x-2]
            mother = vacPlan[x-1]
            child1 = father[:3] + mother[3:6]
            child2 = mother[:3] + father[3:6]
            #print("Before Mutate")
            #print(child1)
            #print(child2)
            #mutate the gene of child for this case we use random from 0 -5
            pos_to_mutate = randint(0, 5)
            child1=mutate(pos_to_mutate,child1)
            child2=mutate(pos_to_mutate,child2)
            #print("After mutate")
            child1.append(fitness(child1))
            totalFitness+=fitness(child1)
            if(child1[6]==0):
                bestSolution.append(child1)
                bestFound=False
            #print(child1)
            child2.append(fitness(child2))
            totalFitness+=fitness(child2)
            if(child2[6]==0):
                bestSolution.append(child2)
                bestFound=False
            #print(child2)
            newGeneration.append(child1)
            newGeneration.append(child2)
            
        #print("New generation for set 1")
        #print(newGeneration)
        vacPlan=newGeneration
        overallFitness.append( ['p'+str(totalTimeRan)+'gen',totalFitness/100] )
        looptime= looptime+1

    end_time = time.time()
    timeTaken= end_time - start_time
    data.append([bestSolution[0][0],bestSolution[0][1],bestSolution[0][2],bestSolution[0][3],bestSolution[0][4],bestSolution[0][5],looptime,timeTaken])

    """
    below is selection by tournament (select pair from top best fitting)
    """
    
    start_time = time.time()
    looptime=0
    bestSolution =[]
    bestFound = True
    vacPlan= copy.deepcopy(gen1VacPlan)
    while bestFound:
        totalFitness=0
        newGeneration = []
        #0-99 in index crossover and mutate
        for x in range(50):
            father = tournamentSelect(vacPlan)
            while True:
                mother = tournamentSelect(vacPlan)
                if(father != mother):
                    break
            child1 = father[:3] + mother[3:6]
            child2 = mother[:3] + father[3:6]
            #print("Before Mutate")
            #print(child1)
            #print(child2)
            #mutate the gene of child for this case we use random from 0 -5
            pos_to_mutate = randint(0, 5)
            child1=mutate(pos_to_mutate,child1)
            child2=mutate(pos_to_mutate,child2)
            #print("After mutate")
            child1.append(fitness(child1))
            totalFitness+=fitness(child1)
            if(child1[6]==0):
                bestSolution.append(child1)
                bestFound=False
            #print(child1)
            child2.append(fitness(child2))
            totalFitness+=fitness(child2)
            if(child2[6]==0):
                bestSolution.append(child2)
                bestFound=False
            #print(child2)
            newGeneration.append(child1)
            newGeneration.append(child2)
        vacPlan=newGeneration
        overallFitness.append( ['m'+str(totalTimeRan)+'gen',totalFitness/100] )
        looptime= looptime+1
    end_time = time.time()
    timeTaken= end_time - start_time
    data.append([bestSolution[0][0],bestSolution[0][1],bestSolution[0][2],bestSolution[0][3],bestSolution[0][4],bestSolution[0][5],looptime,timeTaken])
    
    """
    below is selection by random pairing (select pair by random)
    """
    
    start_time = time.time()
    looptime=0
    bestSolution =[]
    bestFound = True
    while bestFound:
        totalFitness=0
        newGeneration = []
        #0-99 in index crossover and mutate
        for x in range(50):
            father = random.choice(vacPlan)
            while True:
                mother = random.choice(vacPlan)
                if(father != mother):
                    break
            child1 = father[:3] + mother[3:6]
            child2 = mother[:3] + father[3:6]
            #print("Before Mutate")
            #print(child1)
            #print(child2)
            #mutate the gene of child for this case we use random from 0 -5
            pos_to_mutate = randint(0, 5)
            child1=mutate(pos_to_mutate,child1)
            child2=mutate(pos_to_mutate,child2)
            #print("After mutate")
            child1.append(fitness(child1))
            totalFitness+=fitness(child1)
            if(child1[6]==0):
                bestSolution.append(child1)
                bestFound=False
            #print(child1)
            child2.append(fitness(child2))
            totalFitness+=fitness(child2)
            if(child2[6]==0):
                bestSolution.append(child2)
                bestFound=False
            #print(child2)
            newGeneration.append(child1)
            newGeneration.append(child2)
            
        #print("New generation")
        #print(newGeneration)
        vacPlan=newGeneration
        overallFitness.append( ['r'+str(totalTimeRan)+'gen',totalFitness/100] )
        looptime= looptime+1
    end_time = time.time()
    timeTaken= end_time - start_time
    data.append([bestSolution[0][0],bestSolution[0][1],bestSolution[0][2],bestSolution[0][3],bestSolution[0][4],bestSolution[0][5],looptime,timeTaken])
    
totalLoop1,totalLoop2,totalLoop3,totalTime1,totalTime2,totalTime3=[0]*6
for x in range(5):
    totalLoop1 = totalLoop1+data[x*3][6]
    totalLoop2 = totalLoop2+data[x*3+1][6]
    totalLoop3 = totalLoop3+data[x*3+2][6]
    totalTime1 = totalTime1+data[x*3][7]
    totalTime2 = totalTime2+data[x*3+1][7]
    totalTime3 = totalTime3+data[x*3+2][7]
print(data)
print(totalLoop1/5)
print(totalLoop2/5)
print(totalLoop3/5)
print(totalTime1/5)
print(totalTime2/5)
print(totalTime3/5)
with open("q1data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
with open("q1gen.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(overallFitness)